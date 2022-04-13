'''
A quiet student is the one who took at least one exam and did not score the high or the low score.

Write an SQL query to report the students (student_id, student_name) being quiet in all exams. Do not return the student who has never taken any exam.

Return the result table ordered by student_id.

The query result format is in the following example.
'''



WITH cte AS(
    SELECT exam_id, exam.student_id, student_name, score, RANK() OVER(PARTITION BY exam_id ORDER BY score) rk1, RANK() OVER(PARTITION BY exam_id ORDER BY score DESC) rk2 
    FROM exam LEFT JOIN student
    ON exam.student_id = student.student_id
)

SELECT DISTINCT student_id, student_name
FROM cte
WHERE student_id NOT IN (SELECT student_id FROM cte WHERE rk1 = 1 or rk2 = 1)
ORDER BY student_id

---------------------

WITH cte AS 
(
	SELECT exam_id, student_id, 
	RANK() OVER(partition by exam_id order by score DESC) AS "high_score",
	RANK() OVER(partition by exam_id order by score) AS "low_score"
	FROM Exam 
)

SELECT DISTINCT e.student_id, s.student_name
FROM Exam e LEFT JOIN Student s ON s.student_id = e.student_id
WHERE e.student_id NOT IN (SELECT student_id FROM cte WHERE high_score = 1 OR low_score = 1)


--------------------
Select e.student_id, s.student_name from 
Exam e, student s,
(Select max(score) as high, min(score) as low, exam_id from Exam
group by exam_id) r
where 
	e.student_id = s.student_id 
	and e.exam_id = r.exam_id 
group by e.student_id, s.student_name
having sum(Case when e.score = r.high then 1 else 0 end) =0 and
sum(Case when e.score = r.low then 1 else 0 end)= 0 
order by e.student_id
