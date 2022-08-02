'''
Вывести 2 по размеру зарплату.

'''

select salary from (

select salary, rank()over(order by salary desc)as r from employee )k
where r= 2
