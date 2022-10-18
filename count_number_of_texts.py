'''
Alice is texting Bob using her phone. The mapping of digits to letters is shown in the figure below.


In order to add a letter, Alice has to press the key of the corresponding digit i times, where i is the position of the letter in the key.

For example, to add the letter 's', Alice has to press '7' four times. Similarly, to add the letter 'k', Alice has to press '5' twice.
Note that the digits '0' and '1' do not map to any letters, so Alice does not use them.
However, due to an error in transmission, Bob did not receive Alice's text message but received a string of pressed keys instead.

For example, when Alice sent the message "bob", Bob received the string "2266622".
Given a string pressedKeys representing the string received by Bob, return the total number of possible text messages Alice could have sent.

Since the answer may be very large, return it modulo 109 + 7.
'''


class Solution:
    def countTexts(self, A: str) -> int:
        mp = set(["2", "22", "222",
                  "3", "33", "333",
                  '4', '44', '444',
                  '5', '55', '555',
                  '6', '66', '666',
                  '7', '77', '777', '7777', 
                  '8', '88', '888', 
                  '9', '99', '999', '9999'])
        MOD = 10**9+7
        
        @cache
        def dp(i):
            if i>=len(A): return 1
            ans = 0
            if i+1<=len(A) and A[i:i+1] in mp: ans += dp(i+1)%MOD
            if i+2<=len(A) and A[i:i+2] in mp: ans += dp(i+2)%MOD
            if i+3<=len(A) and A[i:i+3] in mp: ans += dp(i+3)%MOD
            if i+4<=len(A) and A[i:i+4] in mp: ans += dp(i+4)%MOD
            return ans%MOD
        
        return dp(0)%MOD
-----------------------------------------------------------------------------------------------------

Let us imagine pressedKeys is "2222".

The only way to interpret "2" is:
["a"]

There are two ways we interpret "22":
["aa", "b"]

Four ways we interpret "222":
["aaa", "ba", "ab", "c"]

7 ways we interpret "2222":
["aaaa", "baa", "aba", "ca", "aab", "bb", "ac"]

In each state we can see that to get the ways a digit is interpretting as ending with "a", we need to combine all digits that ended previously with "a", "b", & "c". Then to get the ways the str can be interpretted as ending with "b", it would be the number of strings that ended with "b" in our previous digit. Similarly for "c" we need to get the number of ways the previous str ended with "b".

So how do we calculate one state from another?
So for the digit "2" in every subsequent digit of "2" to get the new combinations we just check how many previous digits ended with "a", "b", & "c". Same idea goes for every other digit except for "7" and "9" in which case there are 4 transitions, so we need to account and check for one more digit.

When we see a new digit, i.e. if after seeing "222" we then encounter a "3", then we reset our states to be all 0, and make our first state to be the combination of all the previous state endings. Meaning if we had "222" then the possible combinations we have is ["aaa", "ba", "ab", "c"], however whenever we encounter a "3", then they all must end with "d", and as such we now get ["aaad", "bad", "abd", "cd"]. Which then is repersented as [4, 0, 0], meaning we have 4 digits that end with "d", and 0 digits that end "e" & "f".

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        if not pressedKeys:
            return 0
        
        MOD = 10 ** 9 + 7
        chars_in_digit = {'2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 4, '8': 3, '9': 4}
        
        prev_states = [1]
        prev_digit = None
        
        for digit in pressedKeys:
            total = sum(prev_states) % MOD
            
            if digit != prev_digit:
                prev_states = [total] + [0] * (chars_in_digit[digit] - 1)
            else:
                prev_states = [total] + prev_states[:chars_in_digit[digit] - 1]
                
            prev_digit = digit
        
        return sum(prev_states) % MOD
      
----------------------------------------------------------------------------------------------------

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        dp = [0 for _ in range(len(pressedKeys) + 1)]
        dp[0], dp[1] = 1, 1
        for i in range(1, len(pressedKeys) + 1):
            dp[i] = dp[i - 1]
            if i >= 2 and pressedKeys[i - 1] == pressedKeys[i - 2]:
                dp[i] += dp[i - 2]
            else:
                continue
            if i >= 3 and pressedKeys[i - 1] == pressedKeys[i - 3]:
                dp[i] += dp[i - 3]
            else:
                continue
            if i >= 4 and (pressedKeys[i - 1] == '7' or pressedKeys[i - 1] == '9') and pressedKeys[i - 1] == pressedKeys[i - 4]:
                dp[i] += dp[i - 4]
            else:
                continue
        return dp[len(pressedKeys)] % (10 ** 9 + 7)
      
