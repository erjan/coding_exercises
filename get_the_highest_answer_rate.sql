'''

The answer rate for a question is the number of times a user answered the question by the number of times a user showed the question.

Write an SQL query to report the question that has the highest answer rate. If multiple questions have the same maximum answer rate, report the question with the smallest question_id.

The query result format is in the following example.

'''

# Write your MySQL query statement below



with h as(
select

question_id,
sum(if(answer_id is not null ,1,0)) /
count(question_id) as total

from surveylog

group by question_id)



select question_id as survey_log from h
order by total desc limit 1

