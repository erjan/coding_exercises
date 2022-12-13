'''
Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.
'''

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        #the deque keeps track of the set of strings that we want to perform swaps on
        #at the start, the deque contains only s1
        deque = collections.deque([s1])
        
        #this set wasn't mentioned in the "intuition" part. it helps us avoid doing repeated work by adding the same strings to our deque
        seen = set() 
        
        answ=0 #counter for the number of "swaps" done so far
        
        
        while deque:
            for _ in range(len(deque)): #loops through each string in the deque
                
                string = deque.popleft() #gets the first string in the deque
                if string ==s2: return answ
                
                #finds the first non-matching letter in s1
                #this satisfies condition 1 of a "useful" swap
                #ex: this would be s1[3] in the above example
                i=0
                while string[i]==s2[i]:
                    i+=1
                
                #checks all the other letters for potential swaps
                for j in range(i+1, len(string)):
                    if string[i]==s2[j]!=s1[j]: #checks conditions 2 and 3 of a useful swap
                        
                        #swaps the letters at positions i and j
                        new = string[:i] + string[j] + string[i+1:j] + string[i] + string[j+1:]
                        
                        #adds the "new string" if it was not previously added
                        if new not in seen:
                            seen.add(new)
                            deque.append(new)
            
            #record that one more swap was done for each string in the deque
            answ+=1
            
-------------------------------------------------------------------------------------------------------


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        n = len(s1)
        arr, s2_arr = list(s1), list(s2)
        min_steps = float('inf')
        
        def helper(steps,i):
            nonlocal min_steps
            if steps >= min_steps: return
			
            if i == n:
                min_steps = min(min_steps, steps)
                return
				
			# if character at index i is already correct
            if arr[i] == s2[i]:
                helper(steps,i+1)
                return
                
            for j in range(i+1,n):
				'''
				skip if:
					1. characters at i and j are the same
					2. character at j is not what we need at i
					3. character at j is already correctly placed
				'''
                if arr[i] == arr[j] or arr[j] != s2[i] or arr[j] == s2[j]: continue
                    
                arr[i], arr[j] = arr[j], arr[i]
                helper(steps+1,i+1)
                arr[i], arr[j] = arr[j], arr[i]
  
        helper(0,0) 
        return min_steps
