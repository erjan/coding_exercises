
'''

Write an SQL query that reports the books that have sold less than 10 copies in the last year, excluding books that have been available for less than one month from today. Assume today is 2019-06-23.

Return the result table in any order.

The query result format is in the following example.

'''

select b.book_id, b.name

from books b left join orders o

on b.book_id = o.book_id and dispatch_date between '2018-06-23' and '2019-06-23' #this means last year

where datediff('2019-06-23', available_from) > 30

group by b.book_id, b.name

having ifnull(sum(quantity),0) <10;



#another

select b.book_id, b.name from
(select * from books where available_from < '2019-05-23') b
left join
(select * from Orders where dispatch_date > '2018-06-23') o
on b.book_id = o.book_id
group by b.book_id, b.name
having sum(o.quantity) is null or sum(o.quantity) <10;
