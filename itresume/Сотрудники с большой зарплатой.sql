#Необходимо вывести имена всех сотрудников, у которых зарплата больше, чем у их менеджеров.


SELECT w.Name as employee
FROM Employee w,
     Employee m
WHERE w.ManagerId = m.Id
  AND w.salary> m.salary;
