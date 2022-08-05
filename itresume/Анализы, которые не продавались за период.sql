Вывести название всех анализов, которые не продавались с 1 по 3 мая 2020 года.



with help as(

select ord_an,ord_id, ord_datetime from  orders o 
where ord_datetime between '2020-05-01' and '2020-05-03')

select an_name from help right join analysis a on a.an_id = help.ord_an
where ord_id is null
order by an_name
