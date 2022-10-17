'''
You have an initial power of power, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the largest possible score you can achieve after playing any number of tokens.
'''

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score=0
        tokens.sort()
        i=0
        j=len(tokens)-1
        mx=0
        while i<=j:
            if tokens[i]<=power:
                power-=tokens[i]
                score+=1
                i+=1
                mx=max(mx,score)
            elif score>0:
                score-=1
                power+=tokens[j]
                j-=1
            else:
                break
        return mx
      
-------------------------------------------------------------------

Explanation
We want to sort the tokens, because whenever we can't take a reward, we would like to exchange 1 score for the maximum power gained.
We would also want to pay the least for 1 score gained.

With this observation we will sort the tokens array and have 2 pointers.
We greedily pay for the lowest tokens and gain score, whenever we can't take we exchange 1 score for the highest power reward.

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l = 0
        r = len(tokens) - 1
        max_ans = score = 0
        
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                max_ans = max(max_ans, score)
                l += 1
            elif score > 0:
                power += tokens[r]
                r -= 1
                score -= 1
            else:
                break
        
        return max_ans
