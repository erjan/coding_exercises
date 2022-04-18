'''
Given strings s1 and s2, return the minimum contiguous substring part of s1, so that s2 is a subsequence of the part.

If there is no such window in s1 that covers all characters 
in s2, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.
'''


2-steps:

Find a subsequence in S that contains T, and return ending index in S
Improve that subsequence by searching backwards from right-left to find best starting index in S
e.g.
i = 0 1 2 3 4 5 6 7 8 9
S = a b a c b c d f e g
T = bcde
find subsequence - bacbcdfe, end = 8
improve subsequence - bcdfe, start = 4
length = 5

Repeat next subsequence search at index 5 (start+1)

def minWindow(self, S, T):
	
    # Find - Get ending point of subsequence starting after S[s]
    def find_subseq(s):
        t = 0
        while s < len(S):
            if S[s] == T[t]:
                t += 1
                if t == len(T):
                    break
            s += 1
        
        return s if t == len(T) else None       # Ensure last character of T was found before loop ended
    
    # Improve - Get best starting point of subsequence ending at S[s]
    def improve_subseq(s):
        t = len(T) - 1
        while t >= 0:
            if S[s] == T[t]:
                t -= 1
            s -= 1
        
		return s+1
    
    s, min_len, min_window = 0, float('inf'), ''
    
    while s < len(S):
        end = find_subseq(s)            # Find end-point of subsequence
        if not end:
            break
            
        start = improve_subseq(end)     # Improve start-point of subsequence

		if end-start+1 < min_len:       # Track min length
            min_len = end-start+1
            min_window = S[start:end+1]
        
        s = start+1                     # Start next subsequence search

    return min_window
  -----------------------------------------------------------------------------
  class Solution:
    def minWindow(self, S: str, T: str) -> str:
        def dfs(i, j):
            if j == len(T): return i
            if (i, j) not in memo:
                ind = S.find(T[j], i + 1)
                memo[(i, j)] = float('inf') if ind == -1 else dfs(ind, j + 1)
            return memo[(i, j)]
            
        l, res, memo = float('inf'), '', {}
        for i, s in enumerate(S):
            if s == T[0]:
                j = dfs(i, 1)
                if j - i < l:
                    l, res = j - i, S[i:j + 1]
        return res
      
-------------------------------------------------------------
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        queue = collections.deque()
        seen = set()
        for i in range(len(S)):
            if S[i] == T[0]:
                state = (i,0) #lastVisitedInS, lastVisitedInT
                queue.append((i, state)) # begin, state
                seen.add(state)
        
        steps = 0
        while queue:
            L = len(queue)
            for _ in range(L):
                begin, state  = queue.popleft()
                index1, index2 = state
                if index2 == len(T) - 1:
                    return S[begin:index1 + 1]
                
                next1, next2 = index1 + 1, index2 + 1
                
                if next1 < len(S) and next2 < len(T):
                    if S[next1] == T[next2]:
                        newState = (next1, next2)
                    else:
                        # do not skip on next in T
                        newState = (next1, index2)
                    
                    if newState not in seen:
                        seen.add(newState)
                        queue.append((begin, newState))
                    
            steps += 1
        
        return ""
      
------------------------------------------------------------------------
Minimum Window Subsequence
I found this code from the fastest python submissions for this question

Code
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        window = ""
        start = -1
        while True:
            # Searching s1 for each s2 char
            for char in s2:
                start = s1.find(char, start+1)
                # If you can't find all s2 chars, return
                if start == -1:
                    return window
            # Start is currenlty the idx of last s2 char
            end = start; start+=1
            # Find the idx of the first char of s2
            for char in reversed(s2):
                start = s1.rfind(char, 0, start)
            # Update min length
            if not window or len(window) > end-start+1:
                window = s1[start:end+1]
            # Repeat process from next idx
            start += 1
Breakdown
Constraints
- Return min seg of s1 that contains s2
- If multiple segs, return the leftmost
- If no segments, return ""
Approach:
- Optimized Find
  - Find each char of s2, giving you the end char idx
  - rfind the start of that segment 
  - Record the length and repeat
  - Time, space: o(n), o(1)
*I am not sure on the time complexity

Steps
Setup some vars to keep track of your min window
While True
For each char in s2
Find the start of the char in s1, starting from the previous start (plus 1)
If you can't find it, return ans
Update the end var; inc start
For the chars in s2 reversed
Find the start of the char in s1 from 0 to start. (rfind, which returns the highest index found)
Update your min
Inc start
return ans
Mistakes
Not initlizing start to -1
On the first s1.find, not adding one to start
Forgetting to += start before finding the end and after
Forgetting to assign the results of find back to start
In the second rfind loop, you're finding the start, not the end
Explanation
For each char in s2 (what you are looking for)
Find the char in s1, starting from the previous found character start position
Explanation: if you are searching for 'abc'
Find 'a' in the string (let's say it's at index 5)
Then search for 'b' in the string from idx 5 to the end (let's say it's at index 7)
Then search for 'c' in the string from idx 7 to the end.
Since we now have the position of the last char in the segment, we have to find the start position again
The reason we find it again is so we get the earliest position the string could start at.
Explanation: Let s1= 'aabc' and s2='abc'
The first 'a' we find is at idx 0, and the final 'c' is at idx 3
If we go backwards and rfind each character, the start idx would be 1
rfind returns the last index where the substring was found
So you would do something like s1.rfind(char, 0, prev_idx)
Now you have a valid segment. There still could be more segments however, so you would repeat the process, but start from the end index of the current segment.
You would stop processing when you can no longer find a s2 char in the search segment of s1
You don't have to use find or rfind , you could use a while loop instead. I would recommend using the find functions as it would produce clearer code.


-----------------------------------------------------------------------------------------------
The idea is to exhaust the S string until we find subsequence of T. and then exhaust backwards to find the minimum subsequence as per the question.

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        if len(T) > len(S): return ""
        
        sp = tp = 0
        ri, rlen = None, float('inf')
        
        while sp < len(S):
            char = S[sp]
            if char == T[tp]:
                tp += 1
                
            if tp == len(T):
                end_index = sp
                tep = tp - 1
                tp = 0
                
                while tep >=0:
                    # we need to exhaust backwards to find minumum subsequence
                    if T[tep] == S[sp]:
                        tep -= 1
                    
                    sp -= 1
                
                slen = (end_index - sp)
                
                if slen < rlen:
                    rlen = slen
                    ri = (sp + 1, end_index)
                
                sp += 2
        
            sp += 1
        
        if not ri:
            return ""
        
        return S[ri[0]:ri[1] + 1]
      
-------------------------------------------------------------------------------------
class Solution:
    def minWindow(self, S: str, T: str) -> str:
	    # candidates are indexes of the first letter in T
        candidates = collections.deque([index for index in range(len(S)) if S[index] == T[0]])
		if not candidates:
            return ""
		
        leftovers = [i for i in T[1:]]
        if not leftovers:
            return S[candidates[0]]
        
        min_left, min_right = 0, -1
        while candidates:
            index = candidates.popleft()
            q = collections.deque(leftovers)
            r_index = index + 1
            while q:
                next_index = S.find(q.popleft(), r_index)
                if next_index == -1:
                    break
                r_index = next_index + 1
            else:
                if min_right == -1 or min_right - min_left > r_index - index - 1:
                    min_right, min_left = r_index - 1, index   
        
        return S[min_left : min_right + 1]
      

      
      
  
