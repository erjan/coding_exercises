'''
Imagine you have a special keyboard with the following keys:

A: Print one 'A' on the screen.
Ctrl-A: Select the whole screen.
Ctrl-C: Copy selection to buffer.
Ctrl-V: Print buffer on screen appending it after what has already been printed.
Given an integer n, return the maximum number of 'A' you can print on the screen with at most n presses on the keys.
'''


Most solutions out there are Math related or O(N^2), they are either difficult to come up with (especially during an interview) or not as efficient, so I figured to share this pure Dynamic Programming solution.

From my point of view, Dynamic Programming is way easier to think than Math Induction, because Induction takes time and difficult to draw a conclusion for non-obvious question like this.

Explanation
There are only 3 scenarios can put A on screen:
Scenario 1: Simply use key1 to put A
Scenario 2: If we copied something to clipboard in previous step, simply use key4 to paste whatever in the clipboard
Scenario 3: Ctrl A + Ctrl C + Ctrl V -> key2 + key3 + key4. This takes 3 steps to double number of A from 3 steps ago.
Once you understand above, the rest are easy to implement
Note that we need to maintain a 2xN matrix for clipboard information, so that Scenario 2 & 3 know what information they were used before
dp[0][i]: Scenario 1 at step i
dp[1][i]: Scenario 2 at step i
dp[2][i]: Scenario 3 at step i
clipboard[0][i]: Clipboard info for Scenario 2 at step i
clipboard[1][i]: Clipboard info for Scenario 3 at step i
More explanation about Scenario 2
We can either use clipboard from previous step if previous step was also Scenario 2
Or use clipboard from previous step if previous step was Scenario 3
Make sure discuss them differently
if res_s2 <= res_s3 is same as if res_s2 < res_s3 or res_s2 == res_s3 and clipboard[0][i-1] < clipboard[1][i-1]
The reason is clipboard for Scenario 3 will always greater than or equal to clipboard for Scenario 2
Thus, if there is a tie res_s2 == res_s3, we always take Scenario 3
The result is in last step, the largest among 3 scenarios
Time Complexity: O(N)
Space Complexity: O(N)
Implementation
class Solution:
    def maxA(self, N: int) -> int:
        dp = [[0] * (N+1) for _ in range(3)]                              # 3xN matrix to store info of 3 scenarios at each step
        clipboard = [[0] * (N+1) for _ in range(2)]                       # 2xN matrix to store clipboard info of 2nd & 3rd scenarios
        for i in range(1, N+1):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1]) + 1        # scenario1: key1
            if i >= 1:                                                    # scenario2: key4 
                res_s2 = dp[1][i-1] + clipboard[0][i-1]                   # use paste result & clipboard from senario 2
                res_s3 = dp[2][i-1] + clipboard[1][i-1]                   # use paste result & clipboard from senario 3 
                if res_s2 <= res_s3:
                    dp[1][i] = res_s3
                    clipboard[0][i] = clipboard[1][i-1]
                else:    
                    dp[1][i] = res_s2
                    clipboard[0][i] = clipboard[0][i-1]
            if i >= 3:                                                    # scenario3: key2+key3+key4
                clipboard[1][i] = max(dp[0][i-3], dp[1][i-3], dp[2][i-3]) # find out largest value 3 steps before
                dp[2][i] = clipboard[1][i]*2                              # double it
        return max(dp[i][-1] for i in range(3))                           # in last step, max among 3 is the result
      
--------------------------------------------------------------------------------------------------------

This was inspired by https://leetcode.com/problems/4-keys-keyboard/discuss/105982/O(1)-time-O(1)-space-c%2B%2B-solution-possibly-shortest-and-fastest

I will omit the proof that we only need to multiply by 3 or 4.

To get the maximum, we need to multiply 4 as many times as possible. The very first multiply 4 operation takes 4 keys: literal 'A'. The rest multiply 4 operations take 5 keys: Ctrl + 'ACVVV'. So if there are only multiply 4 operations, then (N + 1) % 5 == 0.

If (N + 1) % 5 != 0, then the total number of operations is (N+1)//5 + 1 and some of them will be multiply 3 operations. The multiply 3 operation take 4 keys: Ctrl + 'ACVV'.
If the remainder is 4. Then there is only 1 multiply 3 Op because we don't need to change any of the exsiting multiply 4 Ops.
If the remainder is 3, Then there will be 2 multiply 3 Ops because we need to change one of the existing multiply 4 Op to multiply 3 Op.
You can see that the number of multiple 3 Ops = 5 - remainder.

For example:
If N = 24, the partitions of keys are 4 5 5 5 5, all of them are multiply 4 Ops.
If N = 25, the initial partitions are 4 5 5 5 5 1. We need to reduce the last 3 5 by 1, then add them to the last 1, so that we have 4 5 4 4 4 4, in which the first 2 are multiply 4 Ops, the last 4 are multiply 3 Ops.

class Solution:
    def maxA(self, N: int) -> int:
        if N <= 10:
            return [0, 1, 2, 3, 4, 5, 6, 9, 12, 16, 20][N]
        q, r = divmod(N+1, 5)
        if r == 0:
            return pow(4, q)
        n3 = 5 - r
        return pow(3, n3) * pow(4, q + 1 - n3)
      
      
---------------------------------------------------------------------------      
      
  
class Solution:
    def maxA(self, n: int) -> int:
        # If state is less than any existing, then don't add
        def shouldAdd(states: set(), newstate: (int, int, int)) -> bool:
            for s in states:
                if s[0] >= newstate[0] and s[1] >= newstate[1] and s[2] >= newstate[2]:
                    return False
            return True
        
        # Step has sets of possible states - (selected, buffer, screen)
        state = [set() for _ in range(n + 1)]
        # Initial state
        state[0] = {(0, 0, 0)}
        
        for i in range(n):
            for s in state[i]:
                selected, buffer, screen = s
                
                # Press A
                newstate = (selected, buffer, screen + 1)
                if (shouldAdd(state[i + 1], newstate)):
                    state[i + 1].add(newstate)
                    
                # Press Ctrl-A
                if screen != selected:
                    newstate = (screen, buffer, screen)
                    if (shouldAdd(state[i + 1], newstate)):
                        state[i + 1].add(newstate)

                # Press Ctrl-V
                if buffer != 0:
                    newstate = (selected, buffer, screen + buffer)
                    if (shouldAdd(state[i + 1], newstate)):
                        state[i + 1].add(newstate)

                # Press Ctrl-C
                if selected != buffer:
                    newstate = (selected, selected, screen)
                    if (shouldAdd(state[i + 1], newstate)):
                        state[i + 1].add(newstate)
                        
        # Max screen for last state
        return max([screen for _, _, screen in state[n]])
-------------------------------------------------------------------

    class Solution:
		def maxA(self, n: int) -> int:
			dp = []
			for i in range(n):
				dp.append(i + 1 if i < 6 else max(2 * dp[i - 3], 3 * dp[i - 4], 4 * dp[i - 5]))
			return dp[-1]
    
      
  
