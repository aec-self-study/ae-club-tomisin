{{ config(materialized = 'table')}}

select
    date_trunc(first_order_at, month) as signup_month,
    count(distinct customers.customer_id) as new_customers
from {{ref('int_customers')}} customers
group by 1