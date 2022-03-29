'''
Write an SQL query to report all the consecutive available seats in the cinema.

Return the result table ordered by seat_id in ascending order.

The test cases are generated so that more than two seats are consecutively available.

The query result format is in the following example.

 
 '''




with h as(

select seat_id,
    
    case when (lag(free,1)over(order by seat_id) = 1
    or lead(free,1) over(order by seat_id) = 1)
    and free = 1 then 1 else 0 end as consecutive
    
    from cinema)
    
    
select seat_id from h
where consecutive = 1
    
   
   
#another using self-join

select distinct a.seat_id
from cinema a
join cinema b
on abs(a.seat_id - b.seat_id) = 1
and a.free=true and b.free=true
order by a.seat_id;
