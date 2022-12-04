'''
You are given two strings stamp and target. Initially, there is a string s of length target.length with all s[i] == '?'.

In one turn, you can place stamp over s and replace every letter in the s with the corresponding letter from stamp.

For example, if stamp = "abc" and target = "abcba", then s is "?????" initially. In one turn you can:
place stamp at index 0 of s to obtain "abc??",
place stamp at index 1 of s to obtain "?abc?", or
place stamp at index 2 of s to obtain "??abc".
Note that stamp must be fully contained in the boundaries of s in order to stamp (i.e., you cannot place stamp at index 3 of s).
We want to convert s to target using at most 10 * target.length turns.

Return an array of the index of the left-most letter being stamped at each turn. If we cannot obtain target from s within 10 * target.length turns, return an empty array.
'''


def movesToStamp(stamp, target):
	memo, ls, lt = {}, len(stamp), len(target)
	def dfs(s, t, seqs):
		if t == lt:
			memo[s, t] = seqs if s == ls else []
		if (s, t) not in memo:
			if s == ls:
				for i in range(ls):
					cand = dfs(i, t, [t-i]+seqs)
					if cand:
						memo[s, t] = cand
						break
				else: 
					memo[s, t] = []
			elif target[t] == stamp[s]:
				cand = dfs(s+1, t+1, seqs)
				memo[s, t] = cand if cand else dfs(0, t+1, seqs+[t+1])
			else:
				memo[s, t] = []
		return memo[s, t]
	return dfs(0, 0, [0])

------------------------------------------------------------------------------------------------
class Solution:
    def movesToStamp(self, s: str, t: str) -> List[int]:
        options = {i*'*' + s[i:j] + (len(s)-j)*'*' for i in range(len(s)) for j in range(i, len(s)+1)} - {'*'*len(s)}
        res = []
        target = list(t)
        
        updates = -1
        while updates:
            i = updates = 0
            t = ''.join(target)
            while i <= len(t) - len(s):
                if t[i:i+len(s)] in options:
                    res.append(i)
                    target[i:i+len(s)] = ['*']*len(s)
                    updates += 1
                i += 1
                
        return res[::-1] if set(target) == {'*'} else []
      
-------------------------------------------------------------------------------
There can be two ways either starting from "?????" to target  or we can start from target to "?????"

Now why exactly is going from target to "?????" better ?

See we can get the answer more easily this way . Try for an example by yourself (pen-paper) and do both ways you'll get the answer

Now when we start from our target let's take an example

target:  a b a b a b c b c b a b a b c b c
stamp = a b c

 target:  a b a b a b c b c b a b a b c b c
N = len(target)
M = len(stamp)
 Now we try to traverse the target and check if substring from index i  to index i + M is == our stamp 
 
 Now for checking equality between string = target[i:i+M] and stamp
 if string[index] == stamp[index] : since they are same check index+1
 elif string[index] == "?" : we have solved for this place alredy means even if we write anything here ( since we are doing in reverse order ) in the next step it will  solve for the ?
 else :  they aren't same
  So we will need to iterate through T a number of times, finding and removing any full instances of S. Once we are past the initial pass, we can use character masks to find partial matches for S on each remaining pass.
 
 
  pass 1:  a b a b a b c b c b a b a b c b c
                  ^ ^ ^           ^ ^ ^

 pass 2:  a b a b * * * b c b a b * * * b c
              ^ ^ ^   ^ ^ ^   ^ ^ ^   ^ ^ ^

 pass 3:  a b * * * * * * * b * * * * * * *
          ^ ^ ^           ^ ^ ^

 pass 4:  * * * * * * * * * * * * * * * * *
 
 
 See carefully what we are doing everytime we are finding stamp in our target and making it "????" 
 
 Now the key concept is whenever we find our target and stamp like this
 target = "???ab??"
 stamp = dabc
 
 then "?ab?" == "dabc"
 why ??
 See we are going reverse so the steps we are taking is also reverse
 Since we have put ? anywhere means that we got it right !
 so once we put "dabc" in place of "?ab?" we know that our previous turn is going to solve for the two ? marks any way
 
