'''
There is a country with three schools, where each student is enrolled in exactly one school. The country is joining a competition and wants to select one student from each school to represent the country such that:

member_A is selected from SchoolA,
member_B is selected from SchoolB,
member_C is selected from SchoolC, and
The selected students' names and IDs are pairwise distinct (i.e. no two students share the same name, and no two students share the same ID).
Write an SQL query to find all the possible triplets representing the country under the given constraints.

Return the result table in any order.

The query result format is in the following example.
'''


select schoola.student_name as member_A, 
schoolb.student_name as member_B,
schoolc.student_name as member_C

from schoola cross join schoolb cross join schoolc

where 
schoola.student_id != schoolb.student_id 
and schoolb.student_id != schoolc.student_id
and schoola.student_id != schoolc.student_id


and schoola.student_name   != schoolb.student_name   and 
schoolb.student_name   != schoolc.student_name  
and schoola.student_name   != schoolc.student_name  
