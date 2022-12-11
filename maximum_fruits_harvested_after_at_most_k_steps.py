'''
Fruits are available at some positions on an infinite x-axis. You are given a 2D integer array fruits where fruits[i] = [positioni, amounti] depicts amounti fruits at the position positioni. fruits is already sorted by positioni in ascending order, and each positioni is unique.

You are also given an integer startPos and an integer k. Initially, you are at the position startPos. From any position, you can either walk to the left or right. It takes one step to move one unit on the x-axis, and you can walk at most k steps in total. For every position you reach, you harvest all the fruits at that position, and the fruits will disappear from that position.

Return the maximum total number of fruits you can harvest.
'''

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        ans = rsm = ii = 0 
        for i, (p, x) in enumerate(fruits): 
            if p > startPos + k: break 
            rsm += x
            if p <= startPos: fn = lambda ii: startPos - fruits[ii][0]
            else: fn = lambda ii: min(2*(p-startPos) + (startPos-fruits[ii][0]), (p-startPos) + 2*(startPos-fruits[ii][0]))
            while ii <= i and fn(ii) > k: 
                rsm -= fruits[ii][1]
                ii += 1
            ans = max(ans, rsm)
        return ans 
      
-------------------------------------------------------------------
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        
        f = [0] * (2 * 10**5 + 1)
        for a, b in fruits:
            f[a] = b

        f_acc = list(accumulate(f, initial=0))
        n = len(f_acc)
        
        startPos += 1
        left_only = f_acc[startPos] - f_acc[max(0, startPos - k - 1)]
        right_only = f_acc[min(n - 1, startPos + k)] - f_acc[startPos - 1]
        ans = max(left_only, right_only)
        
        # turn left and then right
        for i in range(1, (k - 1) // 2 + 1):
            
            first_left = f_acc[startPos] - f_acc[max(0, startPos - i - 1)]
            then_right = f_acc[min(n - 1, startPos + k-2*i)] - f_acc[startPos]
        
            first_right = f_acc[min(n - 1, startPos + i)] - f_acc[startPos - 1]
            then_left = f_acc[startPos - 1] - f_acc[max(0, startPos - (k - 2*i) - 1)]
            ans = max(ans, first_left + then_right, first_right + then_left)
        
        return ans
      
--------------------------------------------------------------------------------------------------------

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
    
        fruitMap = defaultdict(int)
        
        for position, amount in fruits:
            fruitMap[position] = amount
        
        
        if k == 0:
            return fruitMap[startPos]
        
        totalLeft = 0 # max sum if we go k steps to the left
        totalRight = 0 # max sum if we go k steps to the right
        inBetween = 0 # max sum if we go x steps to the left & k steps to the right (ensuring that we don't move more than k steps in total)
        
        dp = dict()
        
        for i in range(startPos,startPos-k-1, -1):
            totalLeft += fruitMap[i]
            dp[i] = totalLeft
            
        for i in range(startPos,startPos+k+1):
            totalRight += fruitMap[i]
            dp[i] = totalRight
            
        
        leftSteps = 1
        rightSteps = k-2
        
        while rightSteps > 0:
            currAmount = 0
            
            # go right & collect
            currAmount += dp[startPos-leftSteps]
            # go left & collect
            currAmount += dp[startPos+rightSteps]
            
            
            inBetween = max(inBetween, currAmount-fruitMap[startPos])
            
            leftSteps += 1
            rightSteps -= 2
        
        
        leftSteps = k-2
        rightSteps = 1
        
        while leftSteps > 0:
            currAmount = 0
            
            # go right & collect
            currAmount += dp[startPos-leftSteps]
            # go left & collect
            currAmount += dp[startPos+rightSteps]
            
            inBetween = max(inBetween, currAmount-fruitMap[startPos])
            
            leftSteps -= 2
            rightSteps += 1
        
            
        return max(totalLeft, totalRight, inBetween)
