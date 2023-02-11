'''
The Olympic table is sorted according to the following rules:

The country with more gold medals comes first.
If there is a tie in the gold medals, the country with more silver medals comes first.
If there is a tie in the silver medals, the country with more bronze medals comes first.
If there is a tie in the bronze medals, the countries with the tie are sorted in ascending order lexicographically.
Write an SQL query to sort the Olympic table

The query result format is shown in the following example.
'''

select * from olympic

order by  gold_medals desc, silver_medals desc, bronze_medals desc, country asc
