'''
You are given an array of positive integers price where price[i] denotes the price of the ith candy and a positive integer k.

The store sells baskets of k distinct candies. The tastiness of a candy basket is the smallest absolute difference of the prices of any two candies in the basket.

Return the maximum tastiness of a candy basket.
'''

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        if k == 0:
            return 0
        price.sort()

        def isValid(num):
            n = len(price)
            cnt = 1
            diff = price[0] +num
            for i in range(1,n):
                if price[i] >=diff:
                    diff = price[i]+num
                    cnt+=1
                else:
                    continue
            return cnt
        
        l = 0
        h = max(price)-min(price)
        ans = -1
        while l<=h:
            mid = (l+h)//2
            if isValid(mid)>=k:
                ans = mid
                l=mid+1
            else:
                h=mid-1
        return ans
            
        
