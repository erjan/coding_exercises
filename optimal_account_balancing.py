'''
You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.

Return the minimum number of transactions required to settle the debt.
'''


Build a map balances which sums debts for each person.
Remove any people who have zero balance.
Define a recursive function dfs() to return the minimum cost of balancing accounts.
Recurse as follows on balances:

Base case: return zero if balances is empty. Otherwise,
Search for candidate groups which have balances which sum to zero.
For a candidate group of minimum size, group_size - 1 is the minimum number of transactions necessary to settle balances, and group_size - 1 + dfs(remaining_balances) is the minimum possible result for the candidate group.
Return the minimum result of the search.
In point 2, why is group_size - 1 the minimum number of transactions necessary to settle balances? To construct a sufficient sequence of transactions, make all the candidate elements stand in a line, and have the i th transfer their non-zero balance to the i + 1 th until the last element has the remaining balance. By addition, the balances all resolve to zero. By the commutative property of addition, this works for any line order. This proves that group_size - 1 transactions is sufficient. We can prove that it is necessary by modeling the candidate elements as list of nodes, noting that we need group_size - 1 edges to connect the list, and noting that every list node must be connected for balances to be settled. Thanks to @mmmax for asking this question.

In the code below, functools LRU cache handles memoization. All we need to do is make function dfs() accept hashable arguments. This is the purpose of tuplify: to convert the map into a canonical hashable value in case there are any overlapping subproblems in the DFS.

def minTransfers(self, transactions: List[List[int]]) -> int:

    tuplify = lambda balance: tuple(sorted((k, v) for k, v in balance.items()))

    @lru_cache(None)
    def dfs(balances):
        if not balances:
            return 0
        res = math.inf
        balances = {k: v for k, v in balances}
        for size in range(2, len(balances) + 1):
            for group in itertools.combinations(balances.keys(), size):
                if sum(balances[k] for k in group) == 0:
                    remaining_balances = {k: v for k, v in balances.items() if k not in group}
                    res = min(res, size - 1 + dfs(tuplify(remaining_balances)))
        return res

    balances = collections.defaultdict(int)
    for u, v, z in transactions:
        balances[u] += z
        balances[v] -= z
    return dfs(tuplify({k: v for k, v in balances.items() if v}))
In the inner loop of the DFS, we can make a slight modification to apply an approach of trying to greedily close out any two accounts with inverse balances. As explained in this post, if we find any such pair of balances, we can settle them greedily and continue with the DFS.

def minTransfers(self, transactions: List[List[int]]) -> int:

			# ... unchanged ...

            for group in itertools.combinations(balances.keys(), size):
                if sum(balances[k] for k in group) == 0:
                    remaining_balances = {k: v for k, v in balances.items() if k not in group}
                    res = min(res, size - 1 + dfs(tuplify(remaining_balances)))
                    if len(group) == 2: # added
                        return res

			# ... unchanged ...
			
One other pruning trick which improves performance:

def minTransfers(self, transactions: List[List[int]]) -> int:

		# ... unchanged ...

        for size in range(2, len(balances) + 1):
            if res <= size - 1: # added
                break
            for group in itertools.combinations(balances.keys(), size):
                if sum(balances[k] for k in group) == 0:
                    remaining_balances = {k: v for k, v in balances.items() if k not in group}
                    res = min(res, size - 1 + dfs(tuplify(remaining_balances)))
                    if len(group) == 2: 
                        return res
						
		# ... unchanged ...
		
Time complexity: Letting N be the number of verticies in the graph balance, our time complexity is O(2^N) because we memoize on subsets. Pruning, memoization, and the "precise-close-out" trick help to reduce the runtime considerably.

Thanks to @dodolala for providing a counter-example the previous incorrect version of this solution which greedily selected the smallest group of balances summing to zero in the DFS.




---------------------------------------------------------------------------------------------------------
def minTransfers(self, transactions):
    """
    Get all persons that have outstanding balance + or -, and discard others
    Greedily find smallest group of persons whose balances sum to zero, and set them to zero.
    Do this by getting all combinations of size 2, then size 3 etc. The moment any size group sums to zero,
    recurse on remaining outstanding persons. Because a greedy solution is guaranteed to exist and is optimal
    e.g.
    6->0 : 50, 1->6 : 40, 2->6 : 10, 6->3 : 40, 6->4 : 40, 5->6 : 25, 6->7 : 10, 7->1 : 10
    balance : 0:50, 1:-30, 2:-10, 3:40, 4:10, 5:-25, 6:-35, 7:0
    remove 7 since it's already at 0, and participating in any give/take only increases transaction size
    Then try to find any combination of size 2 that can cancel each other's debts
    e.g. 2 & 4. 4 gives 10 to 2, 1 transaction. Then 2 & 4's balances are set to 0, then remove them.
    Recurse on remaining.
    Again try to find any combinations of size 2. None. So find combinations of size 3, size 4, size 5.
    size 5 - all remaining add up to 90 - 90. 4 transactions
    Total 5 transactions
    """
    
    def outstanding(balance):               # Get all persons with either + or - money
        return {person:money for person,money in balance.items() if money != 0}
    
    def min_trans(balance):
        if not balance:
            return 0
        
        for size in range(2,len(balance)+1):                                # Greedily start from smallest size of 2
            for group in combinations(balance.keys(), size):                # Get all combinations
                if sum(balance[person] for person in group) == 0:           # If they can cancel each others debts
                    for person in group:
                        balance[person] = 0                                 # Set all persons in that group to 0
                    transactions = size-1                                   # Number of transactions needed is size-1
                    return transactions + min_trans(outstanding(balance))   # Recurse on remaining outstanding balances
    
    balance = defaultdict(int)
    for u,v,money in transactions:          # Get final balance of each person
        balance[u] -= money
        balance[v] += money
    
    return min_trans(outstanding(balance))
    
---------------------------------------------------------------------------------------------
The brute force way is the solution.

With using backtracking, we can see all ways of making transaction across different accounts and try to get the minimun number.

Prepped work:

go through the list of transactions, and try to calculate each person's account balance (balance).
go through balance to create a list of amounts (accounts) that contains none zero amounts, because if the amount is 0, it has already been settled.
BACKTRACKING:
In each recursive function, you can think of it as finding the minimum number of transactions to settle debt form start to len(accounts) (accounts[start:])

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        def dfs(start):
            r"""
            Recursive function will return the minimun number of transactions needed 
			to make all([a == 0 for a in accounts[start:]])
            """
            # If your start index reach to end, return 0
            if start == len(accounts):
                return 0
            cur_balance = accounts[start]
            # If your start index is cleared, clear following debts
            if cur_balance == 0:
                return dfs(start + 1)
            
            min_trans = float('inf')
            # Going through following account amount, 
			# to see if you can use the combinations
            # to get the minimun number of transactions to cleared accounts[start:]
            for i in range(start + 1,  len(accounts)):
                next_balance = accounts[i]
                # The current balance can be reduced only when next balance and current balance are different sign 
                if (cur_balance * next_balance) < 0:
                    # accounts[start] makes a transaction to accounts[i] => 1 transaction
                    accounts[i] += cur_balance
                    # move to next position to cleared accounts[(start + 1):]
                    min_trans = min(min_trans, 1 + dfs(start + 1))
                    # recovered to try with clearing this with other position
                    accounts[i] -= cur_balance
                    
                    # A way to prune: 
					# when your accounts[start] == accounts[i], transaction between start and i should be the best case; 
					# therefore, no need to look for following combinations
                    if cur_balance + next_balance == 0:
                        break
            return min_trans
                
        # balance[k] = the amount of debt k currently has
        balance = collections.Counter()
        for f, t, a in transactions:
            balance[f] -= a 
            balance[t] += a
        
        accounts = [val for a, val in balance.items() if val != 0]

        return dfs(0)
        
---------------------------------------------------------------------------------------------------------------------
Thanks to the post https://leetcode.com/problems/optimal-account-balancing/discuss/1000293/C++-8ms-Very-Straightforward-Iterative-Solution, it provides a very straight forward thinking.
Based on the solution, I created python version.

This problem boils down to:

Process all transactions to generate final balances.
Remove all zero balances.
Find the smallest subset of balances that sums to 0, start from group of 2. (Here we just use itertools.combinations to generate all possible combinations, and pick sub groups if the sum is 0)
Remove these from the set of balances. Since we generated all possible combinations, we need to be careful when removing them, because some of the sub groups doesn't exist anymore when you start removing elements. Why we can't immediately remove the sub group as soon as we find it? Because it will change the size of balance, which would make the itertools lost track.
If we have any balances left, go to Step 3 and increase group size.
The result in each step is sub gourp size - 1, for example, if we have 2 balances in a sub group, the number of transaction is 1. Why? I'm not fully understood either, I just know the min edges to connect each point in a group(size of n) without a circle is n-1, not sure why the rule applies here.
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:    
        # calculate final balance
        counter = defaultdict(int)        
        for t in transactions:
            counter[t[0]] -= t[2]
            counter[t[1]] += t[2]        
        
        # only get outstanding balances
        balance = [x for x in list(counter.values()) if x != 0]        
        
        ans = 0
        
        # find smallest sub groups, min with 2 elements, max with all elements 
        for r in range(2, len(balance)+1):
            group = set()
            
            # find all possible combinations, if a sub group has sum of 0, pick them as candidate
            group.update(g for g in itertools.combinations(balance, r) if sum(g) == 0)

            # remove sub group from balance, only remove a sub group when all elements in the sub gourp are still in balance
            for g in group:
                if all([c in balance for c in g]):                    
                    for c in g:
                        balance.remove(c)
                    ans += len(g) - 1 
                    
        return ans
        
        
-------------------------------------------------------------------------------------------------------------------------------------
Python DP solution
1. Caculate Final Accounts
First, we figure out those who will always need to transact, we can do this by computing:

owes people who ultimately owe money to the collective and the total amount they owe.
need people who are ultimately owed money from the collective and the total amount they need.
Basically, if you have lent and borrowed equally, you won't be included in either, if you have lent more than you have borrowed, you will be in need, if you have borrowed more than you have lent, you will be in owes.

2. Match Debts and Loans
Next, we want to know out how these loans should be matched with debts, so that we achieve the minimum number of transactions.

For this, we use dynamic programming and guess every which way. However, if there is a person that owes exactly as much as another person has lent, we don't consider the other guesses and match them straightaway instead as this will always be optimal.

Concise Version
from collections import defaultdict
from functools import lru_cache

class Solution:
    
    def minTransfers(self, transactions: List[List[int]]) -> int:
            
        @lru_cache(None)
        def dp(x, y):
            if not x: return 0
            count = math.inf
            for i in range(len(x)):
                for j in range(len(y)):
                    if x[i] == y[j]:
                        return dp(x[:i] + x[i+1:], y[:j] + y[j+1:]) + 1
        
            for i in range(len(x)):
                if i > 0 and x[i] == x[i-1]: continue
                for j in range(len(y)):
                    if j > 0 and y[j] == y[j-1]: continue
                    next_y = y[:j] + y[j+1:] if x[i] >= y[j] else y[:j] + (y[j]-x[i],) + y[j+1:]
                    next_x = x[:i] + x[i+1:] if x[i] <= y[j] else x[:i] + (x[i]-y[j],) + x[i+1:]
                    count = min(count, dp(next_x, next_y) + 1)     
            return count
        
        need, owes = defaultdict(int), defaultdict(int)        
        for x, y, z in transactions:
            need[x] = max(0, need[x] + (z - owes[x]))
            owes[x] = max(0, owes[x] - z)            
            owes[y] = max(0, owes[y] + (z - need[y]))
            need[y] = max(0, need[y] - z)

        n, o = [x for x in need.values() if x], [x for x in owes.values() if x] 
        n.sort(), o.sort()
        return dp(tuple(n), tuple(o))
Longer Version
Might be easier to follow along for some, also a little faster.

from collections import defaultdict
from functools import lru_cache

class Solution:
    
    def minTransfers(self, transactions: List[List[int]]) -> int:

        @lru_cache(None)
        def dp(x, y):
            if not x:
                return 0
            count = math.inf
            for i in range(len(x)):
                for j in range(len(y)):
                    if x[i] == y[j]:
                        return dp(x[:i] + x[i+1:], y[:j] + y[j+1:]) + 1
        
            prev_i, prev_j = 0, 0
            for i in range(len(x)):
                if x[i] == prev_i: continue
                for j in range(len(y)):
                    if y[j] == prev_j: continue
                    if x[i] == y[j]:
                        count = min(count, dp(x[:i] + x[i+1:], y[:j] + y[j+1:]) + 1)
                    elif x[i] > y[j]:
                        count = min(count, dp(x[:i] + (x[i]-y[j],) + x[i+1:], y[:j] + y[j+1:]) + 1)
                    else:
                        count = min(count, dp(x[:i] + x[i+1:], y[:j] + (y[j]- x[i],) + y[j+1:]) + 1)
                    prev_j = y[j]
                prev_i = x[i]
            return count
        
        need, owes = defaultdict(int), defaultdict(int)    
        for x, y, z in transactions:
            if z > owes[x]:
                need[x] += z - owes[x]
                owes[x] = 0
            else:
                owes[x] -= z
                
            if z > need[y]:
                owes[y] += z - need[y]
                need[y] = 0
            else:
                need[y] -= z

        n, o = [x for x in need.values() if x], [x for x in owes.values() if x]
        n.sort(), o.sort()
        return dp(tuple(n), tuple(o))
    
