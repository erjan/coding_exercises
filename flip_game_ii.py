'''
You are playing a Flip Game with your friend.

You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Return true if the starting player can guarantee a win, and false otherwise.

 

Example 1:

Input: currentState = "++++"
Output: true
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
Example 2:

Input: currentState = "+"
Output: false
 

Constraints:

1 <= currentState.length <= 60
currentState[i] is either '+' or '-'.

'''


def canWin(self, s):
    for i in xrange(len(s)-1):
        if s[i]=='+' and s[i+1]=='+' and not self.canWin(s[:i]+'--'+s[i+2:]): return True
    return False
  -----------------------------------------------------------------------------------
  def canWin(self, s):
    return any(not self.canWin(s[:i]+"--"+s[i+2:]) for i in xrange(len(s)-1) if s[i:i+2] == "++")
  -----------------------------------------------------------------------------------
  
  The problem is a Impartial game. In combinatorial game theory, the Sprague–Grundy theorem states that every impartial game under the normal play convention is equivalent to a nim heap of a certain size. The size is called a nimber.
  
  
  --------------------------------------------------------------------
  class Solution:
    def canWin(self, initial_state: str) -> bool:
        @cache
        def play(state):
            for i in range(len(state) - 1):
                if state[i] == "+" and state[i + 1] == "+":
                    new_state = state[:i] + "--" + state[i + 2:]
                    if not play(new_state):
                        return True
            return False
        
        return play(initial_state)
----------------------------------------------------------------------      

Nim is a mathematical game of strategy in which two players take turns removing objects from distinct heaps. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap.

For details about the theorem and nimber see @stellari's post or https://en.wikipedia.org/wiki/Nimber.

The problem then become calculate the nimber of the given 'board' and return if it is equal to zero, for any non zero nimber, player 1 wins.

Since we will recursivly call the function nimber through out the test cases, we can use a static cache to do memoization in order to save time. If every nimber required is already known for string s then the time is just O(n) where n is the length of the string. Calculate nimber(n) from scratch is O(n^2).

import re
memo = [0, 0]

def nimber(self, n):
    size = len(self.memo)
    if n < size:
        return self.memo[n]
    if n > size:
        self.nimber(n - 1)
    ordinals = {self.memo[i] ^ self.memo[n - 2 - i] for i in xrange(n / 2)}
    ans = 0
    while ans in ordinals:
        ans += 1
    self.memo.append(ans)
    return ans

def canWin(self, s):
    ans = 0
    for n in map(len, re.split('-+', s)):
        ans ^= self.nimber(n)
    return ans != 0


# 33 / 33 test cases passed.
# Status: Accepted
# Runtime: 40 ms

-----------------------------------------------------------------------------------


class Solution:
    def canWin(self, s: str) -> bool:
        ## RC ##
        ## APPROACH : RECURSION + MEMOIZATION ## ( rec 844ms, + memo 50ms )
        ## Similar to Leetcode: 464. Can I Win ##
        ## LOGIC ##
        ## 1. If we make a move ( for loop ) and pass next state to other player, if he cannot make move then you win
        ## 2. A player cannot make a move if he fails to find "++"
        
		## TIME COMPLEXITY : O(N^2) ##
		## SPACE COMPLEXITY : O(N^2) ##
        
        def dfs(s):
            
            if(s in visited):
                return visited[s]
                        
            for i in range(0,len(s)-1):
                if(s[i] == "+" and s[i+1] == "+"):
                    if( not dfs(s[:i] + "-" + s[i+2:]) ):   # making change and passing it to next user
                        visited[s] = True
                        return True
            visited[s] = False
            return False        # no "++" found
        visited = {}
        return dfs(s)
      
-------------------------------------------------------------------------      




class Solution:
    def canWin(self, currentState: str) -> bool:
        def flip(l, i):
            return [j for j in l if j not in [i - 1, i, i + 1]]
        dp = {}
        def dfs(l):
            key = ','.join([str(num) for num in l])
            if key in dp:
                return dp[key]
            if not l:
                return False
            for i in l:
                if not dfs(flip(l, i)):
                    dp[key] = True
                    return True
            dp[key] = False
            return False
        return dfs([i for i in range(len(currentState) - 1) if currentState[i] == '+' and currentState[i + 1] == '+'])
      
------------------------------------------------------------------------------------------------------------------------------------      
