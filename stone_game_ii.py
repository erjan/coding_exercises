"""
1140. Stone Game II


min-max dp problem. we use top down memoization

since both players follow the same strategy, we can use recursion to 
maximize our score and minimize the opponents score all 

steps: 
1. preprocess accumulate suffix sum for piles to eliminate redundant computation. 
this represents the remaining possible score for each index.
2. define dp state variables for i, and M, which
represent max stones from piles[i..n] and the remaining score in suffixsum[1...n]
3. both players follow the same stategy. i=0 will be alice, bob will be i+1, etc.
3. for each turn try to maximize the value for i by finding
the minimum of the opponent value and taking the difference
between the suffixsum at that index and that value

x can range in entire [1... 2M] inclusive.
we update m on the fly based on x for the subproblems

the base case allow us to take the remaining score if possible. 

Complexity:
O(n^3) time
O(n^2) space

"""

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # cache postsum
        suffixsum = list(itertools.accumulate(reversed(piles)))[::-1]

        @cache  
        def dfs(i, M):            
            # if allowed to take everything, take everything
            if i + 2 * M >= n:
                return suffixsum[i]
            
            # try to pick value to minmax the other player
            min_opponent_value = inf
            for x in range(1, 2 * M + 1):
                opponent_value = dfs(i + x, max(M, x))
                min_opponent_value = min(min_opponent_value, opponent_value)
            
            my_value = suffixsum[i] - min_opponent_value
                           
            return my_value
                           
        return dfs(0, 1)
      
------------------------------------------------------------------------------------------------------
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = {} 
        def recursion(index,M):
            # if we reached to the end we cannot score any value
            if index == n:
                return 0
            # we search if we have solved the same case earlier
            if (index,M) in dp:
                return dp[(index,M)] 
            # total remaining score is the sum of array from index to the end
            total = sum(piles[index:])           
            # if we can take the complete array it is the best choice
            if index + 2*M >= n :return total
            # my_score is the score we are getting as the player who is playing
            my_score = 0
            for x in range(index,index+2*M):
                # opponent score will be calculated by next recursion
                opponent_score = recursion(x+1,max(M,x-index+1))
                # my_score is the remaining value of total - opponent_score
                my_score = max(my_score,total - opponent_score)          
            # this is memoization part
            dp[(index,M)] = my_score
            # return the score
            return my_score
        
        return recursion(0,1)
