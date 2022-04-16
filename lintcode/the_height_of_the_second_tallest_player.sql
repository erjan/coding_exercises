
'''
Write a SQL query to get the second tallest height in the players (height)
'''


select max(height) as second_height from players where height < (select max(height) from players)
