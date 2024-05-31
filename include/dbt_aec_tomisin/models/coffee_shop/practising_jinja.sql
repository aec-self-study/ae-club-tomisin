{% set product_category = ['coffee beans',  'merch', 'brewing supplies'] %}


select
  date_trunc(sold_at, month) as date_month,
{% for product_category in product_category %}
    sum(case when product_category = '{{product_category}}' then item_price end) as {{product_category.replace(' ', '_')}}_amount,
{% endfor %}

--   sum(case when product_category = 'coffee beans' then item_price end) as coffee_beans_amount,
--   sum(case when product_category = 'merch' then item_price end) as merch_amount,
--   sum(case when product_category = 'brewing supplies' then item_price end) as brewing_supplies_amount

from {{ ref('int_order_items') }}
group by 1