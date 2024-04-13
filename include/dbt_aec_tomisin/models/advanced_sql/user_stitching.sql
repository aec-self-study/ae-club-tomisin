select id, 
        visitor_id,
        case when customer_id is not null then first_value(visitor_id) over (partition by customer_id order by timestamp)
          else visitor_id
          end as user_stitched_vistor_id,
        device_type,
        timestamp,
        page,
        customer_id

from `analytics-engineers-club.web_tracking.pageviews`

-- where customer_id = '724ca571-27ac-4e29-8992-0fdb357b8c5d'

order by 5 desc 

-- limit 50

-- A possible test is to check that for each customer_id, the visitor id is unique. It would require a custome test. Include that next.