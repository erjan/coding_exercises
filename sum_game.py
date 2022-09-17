'''
Alice and Bob take turns playing a game, with Alice starting first.

You are given a string num of even length consisting of digits and '?' characters. On each turn, a player will do the following if there is still at least one '?' in num:

Choose an index i where num[i] == '?'.
Replace num[i] with any digit between '0' and '9'.
The game ends when there are no more '?' characters in num.

For Bob to win, the sum of the digits in the first half of num must be equal to the sum of the digits in the second half. For Alice to win, the sums must not be equal.

For example, if the game ended with num = "243801", then Bob wins because 2+4+3 = 8+0+1. If the game ended with num = "243803", then Alice wins because 2+4+3 != 8+0+3.
Assuming Alice and Bob play optimally, return true if Alice will win and false if Bob will win.
'''

def sumGame(self, num: str) -> bool:
  count, s, n = 0, 0, len(num)
  
  for i,d, in enumerate(num):
    if d == '?': 
	  count += 1 if i < n // 2 else -1
	elif i < n // 2:
	  s += int(d)
	else:
      s -= int(d)
	
  if s * 2 == -9 * count:
    return False
  return True

----------------------------------------------------------------------------------
class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        q_cnt_1 = s1 = 0
        for i in range(n//2):    # get digit sum and question mark count for the first half of `num`
            if num[i] == '?':
                q_cnt_1 += 1
            else:    
                s1 += int(num[i])
        q_cnt_2 = s2 = 0				
        for i in range(n//2, n): # get digit sum and question mark count for the second half of `num`
            if num[i] == '?':
                q_cnt_2 += 1
            else:    
                s2 += int(num[i])
        s_diff = s1 - s2         # calculate sum difference and question mark difference
        q_diff = q_cnt_2 - q_cnt_1
        return not (q_diff % 2 == 0 and q_diff // 2 * 9 == s_diff) # When Bob can't win, Alice wins
