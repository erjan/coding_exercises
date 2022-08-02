'''
Необходимо вывести среднюю стоимость 5-ой покупки с разбивкой по городам.


'''


with rn as(
select * , row_number()over(partition by c.town,c.id_customer order by created_at asc, p.id) as rn
  from purchases p
  left join skus s on p.sku_id = s.id
  left join customer c on p.user_id = c.id_customer
  )
  
  ,filtered_rn as(
  select * from rn where rn =5 
  )
  
  select town, AVG(price) as avg_price_5th_purchase
  from filtered_rn
  group by town
  order by avg_price_5th_purchase desc




