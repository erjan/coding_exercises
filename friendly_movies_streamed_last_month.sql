'''
Write an SQL query to report the distinct titles of the kid-friendly movies streamed in June 2020.

Return the result table in any order.

The query result format is in the following example.

 
 '''


select distinct title from tvprogram join content 

using(content_id)

where year(program_date) = 2020 and month(program_date) = 6 and kids_content = 'Y'
and content_type = 'Movies'
