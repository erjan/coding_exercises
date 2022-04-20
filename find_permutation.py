
'''

A permutation perm of n integers of all the integers in the range [1, n] can be represented as a string s of length n - 1 where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the lexicographically smallest permutation perm and return it.

 
 '''

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        ans, stack = [], []
        for i, ch in enumerate(s + "I"): 
            if ch == "D": stack.append(i+1)
            else: 
                ans.append(i+1)
                while stack: ans.append(stack.pop())
        return ans 
      
-----------------------------------------------------------

Observations:

If all characters were increases then we could just output numbers 1..n.
Decrease messes up the ordering and forces us to put larger numbers upfront.
Solution:
We will start filling out the array from 1 to n iteratively. To account for consecutive decreases we pre-process the array and calculate the forced number increases. For example, the sequence 'IDDI' will have forced increases because of second and third characters. To understand the solution better you may want to print out the res array after pre-processing to get a feel for what it accomplishes.

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n = len(s) + 1
        res = [0] * n
        
        for i in range(n-2, -1, -1):
            res[i] = 0 if s[i] == 'I' else res[i + 1] + 1
        
        cur = 1
        i = 0
        while i < n:
            j = i
            while res[i] > 0:
                res[i] = cur + res[i]
                i += 1
            else:
                res[i] = cur
                i += 1
            cur += (i - j)
            if j == i:  # didn't enter the loop above (i haven't increased)
                res[i] = cur
                cur += 1
                i += 1
        
        return res
      
----------------------------------------------------------

Just for kicks:

Recursive Backtracking Solution:
=> but will sadly yield "Time Limit Exceeded"

class Solution:
    
    def findPermutation(self, s: str) -> List[int]:


        def recurse(s, nums, last):
		
            if len(s) == 0:
                return [last]
            
            current_s = s[0]
            for i in range(len(nums)):
                current_num = nums[i]
                
                if (current_s == 'D' and last > current_num or
                    current_s == 'I' and last < current_num):
                    
                    result = recurse(s[1:], nums[:i]+nums[i+1:], nums[i])
                    if result != []:
                        return [last] + result
                else:
                    return []
                    
        nums = list(range(1,len(s)+2))
        for i in range(len(nums)):
            ans = recurse(s, nums[:i]+nums[i+1:], nums[i])
            if ans: return ans
-------------------------------------------------------------------------

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        ## RC ##
		## APPROACH : STACK ##
        ## LOGIC ##
        ## 1. When we get D, we push and when we get I, we calculate previous maximum value and calculate the next number i.e prev + 1 and add to current I position and as only D's are in the stack and they have lower precedence than I, we pop all incrementing the prev value updated
        ## 2. To simplify the things, I have appended I at the end. ( if there are any D's left in the stack, this will take care and also we are missing out the last number, i.e len(s), so include that aswell we need I at the end)
		
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##

        ## EXAMPLE : "DDIIDDID"	##
		## STACK TRACE ##
        # D [0, 0, 0, 0, 0, 0, 0, 0, 0] [('D', 0)]
        # D [0, 0, 0, 0, 0, 0, 0, 0, 0] [('D', 0), ('D', 1)]
        # I [3, 2, 1, 0, 0, 0, 0, 0, 0] []
        # I [3, 2, 1, 4, 0, 0, 0, 0, 0] []
        # D [3, 2, 1, 4, 0, 0, 0, 0, 0] [('D', 4)]
        # D [3, 2, 1, 4, 0, 0, 0, 0, 0] [('D', 4), ('D', 5)]
        # I [3, 2, 1, 4, 7, 6, 5, 0, 0] []
        # D [3, 2, 1, 4, 7, 6, 5, 0, 0] [('D', 7)]
        # I [3, 2, 1, 4, 7, 6, 5, 9, 8] []

        
        stack = []
        # indicates the value of the last element that is put in the ans array
        prev = 0
        ans = [0] *(len(s)+1)
        for i, ch in enumerate(s + "I"):
            if( ch == "I" ):
                prev = prev + 1
                ans[i] = prev
                while( stack ):
                    prev += 1
                    ans[stack.pop()] = prev
            else:
                stack.append(i)
            # print(ch, ans, stack)
        return ans
    
        ## OTHER SOLUTION ##
        # Reversing the subarray: we first fill all the answer array with 1 to n sequentially, then from the first occurance of D to first occurance of I, we reverse all values including the Dth and Ith position.
        
            
