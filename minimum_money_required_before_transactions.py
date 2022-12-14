'''
You are given a 0-indexed 2D integer array transactions, where transactions[i] = [costi, cashbacki].

The array describes transactions, where each transaction must be completed exactly once in some order. At any given moment, you have a certain amount of money. In order to complete transaction i, money >= costi must hold true. After performing a transaction, money becomes money - costi + cashbacki.

Return the minimum amount of money required before any transaction so that all of the transactions can be completed regardless of the order of the transactions
'''

def minimumMoney(self, transactions: List[List[int]]) -> int:
        
	goodTransactions = [txn for txn in transactions if txn[0] <= txn[1]]
	badTransactions = [txn for txn in transactions if txn[0] > txn[1]]

	badTransactions.sort(key=lambda x: x[1])

	need = 0
	cur_amount = 0

	for cost,cashback in badTransactions:
		cur_amount += cost
		need = max(need,cur_amount)
		cur_amount -= cashback

	if goodTransactions:
		costliest_good_transaction = max(goodTransactions, key=lambda x: x[0])
		cur_amount += costliest_good_transaction[0]  
		need = max(need, cur_amount)

	return need

----------------------------------------------------------------------------------------
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        ans = val = 0 
        for cost, cashback in transactions: 
            ans += max(0, cost - cashback)
            val = max(val, min(cost, cashback))
        return ans + val 
