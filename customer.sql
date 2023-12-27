select date_month
	, sum(is_active : integer) as customers
	, sum(nrr) as nrr
from analytics.fact_nrr
group by 1
