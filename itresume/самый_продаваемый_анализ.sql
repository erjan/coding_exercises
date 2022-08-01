Найти анализ, который продавался больше всего раз за весь период времени.


# решил с подсказкой - долго тупил 
select  analysis.an_id, count(orders.ord_an) as cnt

from Analysis  inner join orders on analysis.an_id = orders.ord_an

group by analysis.an_id
order by cnt desc limit 1
