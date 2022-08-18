'''
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.
'''


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if n >= k - 1 + maxPts: return 1 #the last possible stop-point is k-1, if we roll a maxPts and it will end within n, that means anyway it will end within n with prob 1, there is no need to continue
        dp = [0] * (n + 1) #dp[i] is the probability we reach point i. As we care what's the probability within n, at most we need dp to calculate from 1 to n
        dp[0], curSum = 1, 0 #dp[0] is the probability we reach 0. As we start with 0, we have a probability of 1 reaching 0
        for i in range(1, n + 1):
            if i - 1 < k: # when the previous point hasn't reached k, that means we can still continue to roll, and we'll add that point. Otherwise, when i - 1 already reaches k, then the game stops and we cannot reach status i from  i - 1 (we cannot pick any more number)
                curSum += dp[i - 1]
            if i - 1 >= maxPts: # we can only reach point i from point i - 1, i - 2, ..., i - maxPts. and hence when we calculate point i, we need to make sure the previous points outside of the range drops out
                curSum -= dp[i - 1 - maxPts]
            dp[i] = curSum / maxPts
        return sum(dp[k:]) # we calculate all the probabilities that we la
