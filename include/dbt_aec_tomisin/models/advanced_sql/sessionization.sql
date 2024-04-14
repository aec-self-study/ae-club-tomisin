with
stitched_users as (
  select *

  from {{ ref ('user_stitching')}}
),

previous_time as (
  select *,
          (coalesce((lag(timestamp, 1) over (partition by customer_id order by timestamp)), timestamp)) previous_page_view_timestamp,
          timestamp_diff(timestamp, (coalesce((lag(timestamp, 1) over (partition by customer_id order by timestamp)), timestamp)), minute) time_difference_mins,
          
  from stitched_users
),

with_session_marker as (
  select *,
          cast(coalesce(time_difference_mins > 30, true) as integer) as is_new_session

  from previous_time
),

with_session_number as (
    select
        *,
        sum(is_new_session) over (
            partition by customer_id
            order by timestamp
            rows between unbounded preceding and current row
        ) as session_number,
        coalesce (page = 'order-confirmation', true) purchase_page_identifier

    from with_session_marker
),

with_session_end_start_time as (
  select *,
          first_value(timestamp) over (partition by customer_id, session_number order by timestamp) session_start_time,
          first_value(timestamp) over (partition by customer_id, session_number order by timestamp desc) session_end_time,
          count(distinct page) over (partition by customer_id, session_number) pages_per_session

  from with_session_number
),

with_session_end_identifier as (
  select *,
          coalesce((session_end_time = timestamp), true) is_session_end

  from with_session_end_start_time
),

with_end_in_purchase_status as (
  select *,
          coalesce(((is_session_end is true) and (purchase_page_identifier is true)), true) session_ended_in_purchase

  from with_session_end_identifier
)

select id,
        visitor_id, user_stitched_vistor_id, customer_id,
        device_type, page, timestamp,
        session_number, session_start_time, session_end_time,
        date_diff(session_start_time, session_end_time, minute) session_length_mins,
        pages_per_session, session_ended_in_purchase

from with_end_in_purchase_status
order by customer_id, timestamp desc