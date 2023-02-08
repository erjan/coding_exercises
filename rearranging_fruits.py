'''
You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:

Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
The cost of the swap is min(basket1[i],basket2[j]).
Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

Return the minimum cost to make both the baskets equal or -1 if impossible.


Intuition
We can check each elements using counter.

You can easily come up with exchange two fruits as cheap as possibile.

To achieve this, the simple idea is to exchage larger value fruits and smaller value fruits.

But be careful, you have to check the way to exchange via the cheapest fruits.

You can see that code here

        for v1,v2 in zip(c1,c2):
            ans += min(v1,v2, min_v*2)

''' 


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        b1 = dict(Counter(basket1))
        b2 = dict(Counter(basket2))
        
        tot = Counter(basket1 + basket2)
        
        c1 = []
        c2 = []
        for k, v in tot.items():
            if v % 2 != 0:
                return -1
            b1c = b1.get(k, 0)
            b2c = b2.get(k, 0)
            if b1c == b2c:
                continue
            if b1c > b2c:
                for i in range((b1c - b2c) // 2):
                    c1.append(k)
            else:
                for i in range((b2c - b1c) // 2):
                    c2.append(k)
        c1 = sorted(c1)
        c2 = sorted(c2, reverse=True)
        ans = 0
        min_v = min(basket1 + basket2)
        for v1,v2 in zip(c1,c2):
            ans += min(v1,v2, min_v*2)
        return ans
      
-----------------------------------------------------------------------------------------------------------
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = Counter(basket1)
        for x in basket2: cnt[x] -= 1
        last = []
        for k, v in cnt.items():
            # if v is odd, an even distribution is never possible
            if v % 2 != 0:
                return -1
            # the count of transferred k is |v|/2
            last += [k] * abs(v // 2)
        # find the min of two input arrays as the intermediate
        minx = min(basket1 + basket2)
        # Use quickselect instead of sort can get a better complexity
        last.sort()
        # The first half may be the cost
        return sum(min(2*minx, x) for x in last[0:len(last)//2])
