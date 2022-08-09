'''
перемножить все значения между собой. Ответ необходимо вывести в столбце multiplier.
'''

with recursive A(mult, rn) as
(
select cast(a as bigint) as mult, rn
  from b where rn = 1 union all
  select mult * b.a as mult, b.rn as rn
  from a join b on a.rn+1 = b.rn
),
B as(
select a, row_number() over(order by a) as rn
  from numbers
)

select mult as multiplier     from a where rn = (select max(rn) from a)
