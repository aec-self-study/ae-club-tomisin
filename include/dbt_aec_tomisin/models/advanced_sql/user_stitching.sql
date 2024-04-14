{{ config(materialized = 'table')}}

with
stitched_users as (
  select id, 
          visitor_id,
          case when customer_id is not null then first_value(visitor_id) over (partition by customer_id order by timestamp)
            else visitor_id
            end as user_stitched_vistor_id,
          device_type,
          timestamp,
          page,
          customer_id

  from {{ source ('web_tracking','pageviews') }}
)

select *
from stitched_users

-- A possible test is to check that for each customer_id, the visitor id is unique. It would require a custome test. Include that next.