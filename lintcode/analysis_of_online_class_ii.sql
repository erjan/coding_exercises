'''
The online_class_situations table shows the behavioral activities of some students in online classes.
Each row of data records the number of courses (may be 0) 
that a student has listened to after logging in to the course with the same device on the same day before quitting the online course.
Write a SQL statement to query the date each student The id 
of the device used to log in to the platform for the first time.
'''


select aa.student_id,aa.device_id
from online_class_situations aa
where (student_id,date) in
    (select distinct student_id,min(date) dt
       from online_class_situations
      where  course_number>0
      group by student_id)
