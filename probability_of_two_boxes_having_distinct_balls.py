'''
Given 2n balls of k distinct colors. You will be given an integer array balls of size k where balls[i] is the number of balls of color i.

All the balls will be shuffled uniformly at random, then we will distribute the first n balls to the first box and the remaining n balls to the other box (Please read the explanation of the second example carefully).

Please note that the two boxes are considered different. For example, if we have two balls of colors a and b, and two boxes [] and (), then the distribution [a] (b) is considered different than the distribution [b] (a) (Please read the explanation of the first example carefully).

Return the probability that the two boxes have the same number of distinct balls. Answers within 10-5 of the actual value will be accepted as correct.
'''

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        allComb = comb(sum(balls),sum(balls)//2)
        @lru_cache(None)
        #num of unique balls in boxA-boxB, num of total balls in boxA, num of total balls in boxB, current bucket
        def helper(offset,num1,num2,idx):
            if idx==-1:
                return num1==num2==offset==0
            res = 0
            for k in range(1,balls[idx]):
                res+=helper(offset,num1-balls[idx]+k,num2-k,idx-1)*comb(balls[idx],k)
            res+=helper(offset-1,num1-balls[idx],num2,idx-1)
            res+=helper(offset+1,num1,num2-balls[idx],idx-1)
            return res
        return helper(0,sum(balls)//2,sum(balls)//2,len(balls)-1)/allComb
