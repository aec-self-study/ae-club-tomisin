select ord.customer_id
      , customer.name
      , customer.email
      , min(ord.created_at) first_order_at
      , count(ord.id) number_of_orders
from  customer
left join  ord
on customer.id = ord.customer_id
group by ord.customer_id
        , customer.name
        , customer.email
        
order by first_order_at
limit 10;
