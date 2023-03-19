'''
You are given an integer money denoting the amount of money (in dollars) that you have and 
another integer children denoting the number of children that you must distribute the money to.

You have to distribute the money according to the following rules:

All money must be distributed.
Everyone must receive at least 1 dollar.
Nobody receives 4 dollars.
Return the maximum number of children who may receive exactly 8 dollars if you 
distribute the money according to the aforementioned rules. If there is no way to distribute the money, return -1.
'''

class Solution:
    def distMoney(self, money: int, children: int) -> int: 
        if money < children: return -1 
        ans = 0 
        for j in range(1,children+1):
            if (money - 8) >= children-j:
                money -= 8
                ans += 1 
            else:
                if j == children and money == 4:
                    ans -= 1
                money = 0
                break
        if money > 0:
            ans -= 1
        return ans
      
--------------------------------------------------------------------------------------------------------------
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # cannot give 1 to every child
        if money < children: return -1
        # have more than enough, all child have 8 except 1 child have more
        if money > 8 * children: return children - 1
        # give 1 to every child first
        money -= children
        # find the number of child to reach 8 and the excess amount
        res, extra = divmod(money, 7)
        # if amount is 3 and only one child is not 8, we need two child to seperate money to avoid child having 4
        if extra == 3 and res + 1 == children: return res - 1
        # return the result
        return res
        
