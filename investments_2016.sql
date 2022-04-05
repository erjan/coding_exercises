'''

Write an SQL query to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:

have the same tiv_2015 value as one or more other policyholders, and
are not located in the same city like any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
Round tiv_2016 to two decimal places.

The query result format is in the following example.

'''


select round(sum(TIV_2016),2) as TIV_2016
from insurance i
where (select count(*) from insurance i1 where i.TIV_2015 = i1.TIV_2015)>1 and 
      (select count(*) from insurance i2 where (i.LAT, i.LON) = (i2.LAT, i2.LON))=1


#another

SELECT ROUND(SUM(TIV_2016),2) AS TIV_2016 FROM Insurance a
WHERE EXISTS (SELECT * FROM Insurance WHERE PID <> a.PID AND TIV_2015 = a.TIV_2015)
AND NOT EXISTS (SELECT * FROM Insurance WHERE PID <> a.PID AND (LAT,LON) = (a.LAT,a.LON));
