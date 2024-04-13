-- Weekly revenue split into product categories

{{ config (materialized = 'table') }}

select 
  extract(year from orders.created_at) as sales_year,
  extract(week from orders.created_at) as sales_week,
  products.category as product_category, 
  sum(product_prices.price * orders.total) as total_sales

from {{ source ('coffee_shop', 'order_items') }} as order_items
 
left join {{ source ('coffee_shop', 'orders') }} as orders
    on order_items.order_id = orders.id
 
left join {{ source ('coffee_shop', 'products') }} as products
    on order_items.product_id = products.id

left join {{ source ('coffee_shop', 'product_prices') }} as product_prices
  on order_items.product_id = product_prices.product_id
  and orders.created_at between product_prices.created_at and product_prices.ended_at
 

group by 1, 2, 3
order by 1 desc, 2 desc, 3