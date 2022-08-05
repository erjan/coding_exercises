'''
Найти анализы с наценкой выше 35% или из 7 категории. Если 
какие-то анализы относятся сразу к двум категориям, то их необходимо оставить.
'''


with help as(
select 

a.*,

cast( round( 100.0* (an_price -an_cost)/an_cost,3)as numeric) as markup

from analysis a
),

help2 as(

 select distinct an_id, an_name,  an_cost, an_price, an_group, markup as charge from help 
 where markup> 35
 order by an_id),
 
 help3 as(
 
  select distinct an_id, an_name,  an_cost, an_price, an_group, markup as charge from help 
 where an_group = 7  
  order by an_id)
  
  
select distinct an_id, an_name,  an_cost, an_price, an_group, charge from help2 
union all
select distinct an_id, an_name,  an_cost, an_price, an_group, charge  from help3
 

