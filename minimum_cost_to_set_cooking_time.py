'''
A generic microwave supports cooking times for:

at least 1 second.
at most 99 minutes and 99 seconds.
To set the cooking time, you push at most four digits. The microwave normalizes what you push as four digits by prepending zeroes. It interprets the first two digits as the minutes and the last two digits as the seconds. It then adds them up as the cooking time. For example,

You push 9 5 4 (three digits). It is normalized as 0954 and interpreted as 9 minutes and 54 seconds.
You push 0 0 0 8 (four digits). It is interpreted as 0 minutes and 8 seconds.
You push 8 0 9 0. It is interpreted as 80 minutes and 90 seconds.
You push 8 1 3 0. It is interpreted as 81 minutes and 30 seconds.
You are given integers startAt, moveCost, pushCost, and targetSeconds. Initially, your finger is on the digit startAt. Moving the finger above any specific digit costs moveCost units of fatigue. Pushing the digit below the finger once costs pushCost units of fatigue.

There can be multiple ways to set the microwave to cook for targetSeconds seconds but you are interested in the way with the minimum cost.

Return the minimum cost to set targetSeconds seconds of cooking time.

Remember that one minute consists of 60 seconds.
'''

class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def count_cost(minutes, seconds): # Calculates cost for certain configuration of minutes and seconds
            time = f'{minutes // 10}{minutes % 10}{seconds // 10}{seconds % 10}' # mm:ss
            time = time.lstrip('0') # since 0's are prepended we remove the 0's to the left to minimize cost
            t = [int(i) for i in time]
            current = startAt
            cost = 0
            for i in t:
                if i != current:
                    current = i
                    cost += moveCost
                cost += pushCost
            return cost
        ans = float('inf')
        for m in range(100): # Check which [mm:ss] configuration works out
            for s in range(100):
                if m * 60 + s == targetSeconds: 
                    ans = min(ans, count_cost(m, s))
        return ans

----------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def cost(mins, secs):
            s, curr, res = str(mins * 100 + secs), str(startAt), 0
            for ch in s:
                if ch == curr: res += pushCost
                else:
                    res += (pushCost + moveCost)
                    curr = ch
            return res

        maxmins, ans = targetSeconds // 60, float('inf')
        for mins in range(maxmins + 1):
            secs = targetSeconds - mins * 60
            if secs > 99 or mins > 99: continue
            ans = min(ans, cost(mins, secs))
        return ans        
