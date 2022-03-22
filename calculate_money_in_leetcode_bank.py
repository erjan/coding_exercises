'''
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
'''


#my own solution

class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        q = list()
        for i in range(1, n+1):

            for j in range(i, i+7):
                if len(q) >= (n):
                    print('out')
                    print('total sum of l')
                    print(sum(q))

                    return sum(q)
                else:
                    print(j, end=' ')
                    q.append(j)
            print()

            
class Solution:
    def totalMoney(self, n: int) -> int:
  
        start = 0
        total = 0
        prev = start
        
        for i in range(1,n+1):
            if i%7 == 1:
                start+=1
                total+=start
                prev = start
            else:
                prev+=1
                total+=prev
        return total            
