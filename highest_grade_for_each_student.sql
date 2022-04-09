'''

Write a SQL query to find the highest grade with its corresponding course 
for each student. In case of a tie, you should find the course with the smallest course_id.

Return the result table ordered by student_id in ascending order.

The query result format is in the following example.

'''

SELECT t.student_id, t.course_id, t.grade
FROM 
	(SELECT student_id, course_id, grade, 
	row_number() over (partition by student_id order by grade desc, course_id asc) as r 
	FROM Enrollments) t
WHERE t.r=1
ORDER BY t.student_id asc

---------------------------

SELECT student_id, MIN(course_id) AS course_id, grade
FROM enrollments a
WHERE grade >=ALL(
  SELECT grade
  FROM enrollments b
  WHERE a.student_id=b.student_id
)
GROUP BY student_id, grade
ORDER BY student_id

-----------------------------------

SELECT student_id, MIN(course_id) AS course_id, grade
FROM enrollments
WHERE (student_id, grade) IN (
  SELECT student_id, MAX(grade)
  FROM enrollments
  GROUP BY student_id)
GROUP BY student_id, grade
ORDER BY student_id
