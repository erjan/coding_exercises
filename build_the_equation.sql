'''
You have a very powerful program that can solve any equation of one variable in the world. The equation passed to the program must be formatted as follows:

The left-hand side (LHS) should contain all the terms.
The right-hand side (RHS) should be zero.
Each term of the LHS should follow the format "<sign><fact>X^<pow>" where:
<sign> is either "+" or "-".
<fact> is the absolute value of the factor.
<pow> is the value of the power.
If the power is 1, do not add "^<pow>".
For example, if power = 1 and factor = 3, the term will be "+3X".
If the power is 0, add neither "X" nor "^<pow>".
For example, if power = 0 and factor = -3, the term will be "-3".
The powers in the LHS should be sorted in descending order.
Write an SQL query to build the equation.

The query result format is in the following example.

'''



select
concat(group_concat(term order by power desc separator ''), '=0') as equation
from (
select
CONCAT(case when factor > 0 then '+' else '' end, 
       factor, 
       case when power = 0 then '' else 'X' end, 
       case when power = 0 or power = 1 then '' else '^' end, 
       case when power = 0 or power = 1 then '' else power end
) term,
power
from
terms
order by power desc) t;

--------------------
with cte as
(
    select concat(if(factor > 0, '+', ''),
                  factor,
                  case
                  when power > 1 then concat('X^', power)
                  when power = 1 then 'X'
                  when power < 0 then concat('X^', '(', power, ')')
                  else ''
                  end
                  ) as lhs,
           power
     from Terms
)
select concat(group_concat(lhs order by power desc separator ''), '=0')
       as equation
 from cte
 
 ----------------------------------
 with eq as (
select
power,
CASE WHEN factor > 0 THEN '+' ELSE '' END sign, 
                factor, 
                CASE WHEN power = 1 THEN 'X' 
                WHEN power = 0 THEN '' ELSE CONCAT('X^', power) END power1

from
Terms
) 

SELECT 

concat(group_concat(sign,factor,power1 order by power desc SEPARATOR  ''),'=0' )equation

from eq
