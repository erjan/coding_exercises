'''
A user is eligible for a discount if they had a purchase in the inclusive interval of time [startDate, endDate] with at least minAmount amount.

Write an SQL query to report the number of users that are eligible for a discount.

The query result format is in the following example.
'''



CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      
      select count(distinct user_id)
      from purchases
      where time_stamp between startDate and endDate
      and amount >=minAmount
      
  );
END
