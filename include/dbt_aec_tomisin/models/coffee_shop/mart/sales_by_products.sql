select  
  date_trunc(sold_at, month) as date_month
--   , sum(case when product_category = '{{ category }}' then item_price end) as {{ category | replace(" ", "_") }}_amount,
  
from 
  {{ ref('int_order_items') }}
group by 1