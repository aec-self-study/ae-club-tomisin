-- weekly revenue split up by new versus returning customers.

{{ config (materialized = 'table') }}

with numbered_customer as (
  select 
    extract(year from orders.created_at) as sales_year,
    extract(week from orders.created_at) as sales_week,
    orders.created_at,
    orders.customer_id,
    row_number() over (partition by orders.customer_id order by orders.created_at) newsness_tag,
    product_prices.price * orders.total as revenue

  from {{ source ('coffee_shop', 'order_items') }} as order_items
 
  left join {{ source ('coffee_shop', 'orders') }} as orders
    on order_items.order_id = orders.id
 
  left join {{ source ('coffee_shop', 'products') }} as products
    on order_items.product_id = products.id

  left join {{ source ('coffee_shop', 'product_prices') }} as product_prices
  on order_items.product_id = product_prices.product_id
  and orders.created_at between product_prices.created_at and product_prices.ended_at
),

tagged_customer as (
  select *, 
          case when newsness_tag = 1 then 'New Customer'
          else 'Returning Customer'
          end as customer_type

  from numbered_customer
)

select sales_year,
        sales_week,
        customer_type,
        sum(revenue) revenue

from tagged_customer
group by 1, 2, 3
order by 1 desc, 2 desc, 3

-- where customer_id = 'a02fbdd6-93c6-4cbb-910b-b9d455afe270'
-- '0ba72e2b-3d05-4dd8-83cf-d4dc98a75ea5', 'f473d52c-4311-4ec3-984b-3d09cc55f516'
-- where newsness_tag >= 8
-- order by 1 desc, 2 desc, 3
-- limit 100