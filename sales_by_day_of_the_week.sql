'''
You are the business owner and would like to obtain a sales report for category items and the day of the week.

Write an SQL query to report how many units in each category have been ordered on each day of the week.

Return the result table ordered by category.

The query result format is in the following example.
'''





with help as(

select 

item_category as category, item_id,

dayname(order_date) as week,

ifnull(sum(quantity),0)  as total
from orders right join items using(item_id)

group by item_category, dayname(order_date) )


select 

category as CATEGORY,  

sum( case when week = 'Monday' then total else 0 end) as Monday,
sum( case when week = 'Tuesday' then total else 0 end) as Tuesday,
sum( case when week = 'Wednesday' then total else 0 end) as Wednesday,
sum( case when week = 'Thursday' then total else 0 end) as Thursday,
sum( case when week = 'Friday' then total else 0 end) as Friday,
sum( case when week = 'Saturday' then total else 0 end) as Saturday,
sum( case when week = 'Sunday' then total else 0 end) as Sunday

from help
group by category
order by category

-----------------------------------------
select b.item_category as 'CATEGORY', sum(case when weekday(a.order_date) = 0 then a.quantity else 0 end) as 'MONDAY',
sum(case when weekday(a.order_date) = 1 then a.quantity else 0 end) as 'TUESDAY',
sum(case when weekday(a.order_date) = 2 then a.quantity else 0 end) as 'WEDNESDAY',
sum(case when weekday(a.order_date) = 3 then a.quantity else 0 end) as 'THURSDAY',
sum(case when weekday(a.order_date) = 4 then a.quantity else 0 end) as 'FRIDAY',
sum(case when weekday(a.order_date) = 5 then a.quantity else 0 end) as 'SATURDAY',
sum(case when weekday(a.order_date) = 6 then a.quantity else 0 end) as 'SUNDAY'
from orders a right join items b on a.item_id = b.item_id
group by b.item_category
order by b.item_category

--------------------------------
SELECT i.item_category AS Category,
    SUM(CASE WHEN DAYOFWEEK(o.order_date) = 2 THEN quantity ELSE 0 END) AS Monday,
    SUM(CASE WHEN DAYOFWEEK(o.order_date) = 3 THEN quantity ELSE 0 END) AS Tuesday,
    SUM(CASE WHEN DAYOFWEEK(o.order_date) = 4 THEN quantity ELSE 0 END) AS Wednesday,
    SUM(CASE WHEN DAYOFWEEK(o.order_date) = 5 THEN quantity ELSE 0 END) AS Thursday,
    SUM(CASE WHEN DAYOFWEEK(o.order_date) = 6 THEN quantity ELSE 0 END) AS Friday,
    SUM(CASE WHEN DAYOFWEEK(o.order_date) = 7 THEN quantity ELSE 0 END) AS Saturday,
    SUM(CASE WHEN DAYOFWEEK(o.order_date) = 1 THEN quantity ELSE 0 END) AS Sunday
FROM Items i
LEFT JOIN Orders o
ON i.item_id = o.item_id
GROUP BY i.item_category
ORDER BY i.item_category;

-------------------------
with sales as (
    select
        datename(weekday, o.order_date) as days
        , i.item_category as category
        , isnull(o.quantity, 0) as quantity
    from Orders o
    right join Items i
    on o.item_id = i.item_id
)
select
    CATEGORY
    , isnull(MONDAY, 0) as MONDAY
    , isnull(TUESDAY, 0) as TUESDAY
    , isnull(WEDNESDAY, 0) as WEDNESDAY
    , isnull(THURSDAY, 0)as THURSDAY
    , isnull(FRIDAY, 0) as FRIDAY
    , isnull(SATURDAY, 0) as SATURDAY
    , isnull(SUNDAY, 0) as SUNDAY
from sales
pivot (
    sum(quantity) for days in (    
        MONDAY
        , TUESDAY
        , WEDNESDAY
        , THURSDAY
        , FRIDAY
        , SATURDAY
        , SUNDAY
    )
) as pivot_table

-----------------------------
with cte as (select item_category, ifnull(sum(quantity),0) total , dayname(order_date) weekday
from orders
right join items
on orders.item_id=items.item_id
group by 1,3)

select item_category as Category 
,ifnull(sum(case when weekday='Monday' then total end),0) as Monday  
,ifnull(sum(case when weekday='Tuesday' then total end),0) as Tuesday
,ifnull(sum(case when weekday='Wednesday' then total end),0) as Wednesday
,ifnull(sum(case when weekday='Thursday' then total end),0) as Thursday
,ifnull(sum(case when weekday='Friday' then total end),0) as Friday
,ifnull(sum(case when weekday='Saturday' then total end),0) as Saturday
,ifnull(sum(case when weekday='Sunday' then total end),0) as Sunday

from cte
group by 1
order by category
