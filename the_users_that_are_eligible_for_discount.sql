'''

A user is eligible for a discount if they had a purchase in the inclusive interval of time [startDate, endDate] with at least minAmount amount.

Write an SQL query to report the IDs of the users that are eligible for a discount.

Return the result table ordered by user_id.

The query result format is in the following example.


'''


CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
	# Write your MySQL query statement below.
    
    
    select 
    distinct user_id
    
    from purchases p
    where p.time_stamp between startDate and endDate 
    and amount>=minAmount order by user_id;
    
	
END
