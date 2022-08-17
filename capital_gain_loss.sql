'''
Write an SQL query to report the Capital gain/loss for each stock.

The Capital gain/loss of a stock is the total gain or loss after buying and selling the stock one or many times.

Return the result table in any order.

The query result format is in the following example.

 
 '''
 
select 

stock_name,

sum(if(operation='Sell' , price,0)) - sum(if(operation ='Buy' ,  price,0)) as capital_gain_loss


from stocks
group by stock_name

