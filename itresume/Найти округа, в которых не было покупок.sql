
'''
Необходимо найти названия всех округов, жители которых никогда не совершали покупки в этом магазине.
'''


select c.name from county c where c.county_code not in (

select county.county_code from county inner join customer on county.county_code = customer.county_code 
inner join c_orders on c_orders.id_customer = customer.id_customer inner join 
order_details on order_details.id_orders = c_orders.id_orders where order_details.id_order_details is not null)
