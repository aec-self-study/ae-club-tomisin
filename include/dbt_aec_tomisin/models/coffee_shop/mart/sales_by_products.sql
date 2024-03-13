select  
  date_trunc(orders.created_at,week) as sales_week,
  products.category as product_category,
  sum(order_items.item_price) as total_income
--   , sum(case when product_category = '{{ category }}' then item_price end) as {{ category | replace(" ", "_") }}_amount,
  
from 
    {{ref('stg_orders')}} as orders 
    left join {{ref('int_order_items')}} as order_items
        on orders.order_id = order_items.order_id
    left join {{ref('products')}} as products
        on order_items.product_id = products.product_id
group by
    1,2,3