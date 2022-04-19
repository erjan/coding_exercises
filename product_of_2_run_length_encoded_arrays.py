'''
Run-length encoding is a compression algorithm that allows for an integer array nums with many segments of consecutive repeated numbers to be represented by a (generally smaller) 2D array encoded. Each encoded[i] = [vali, freqi] describes the ith segment of repeated numbers in nums where vali is the value that is repeated freqi times.

For example, nums = [1,1,1,2,2,2,2,2] is represented by the run-length encoded array encoded = [[1,3],[2,5]]. Another way to read this is "three 1's followed by five 2's".
The product of two run-length encoded arrays encoded1 and encoded2 can be calculated using the following steps:

Expand both encoded1 and encoded2 into the full arrays nums1 and nums2 respectively.
Create a new array prodNums of length nums1.length and set prodNums[i] = nums1[i] * nums2[i].
Compress prodNums into a run-length encoded array and return it.
You are given two run-length encoded arrays encoded1 and encoded2 representing full arrays nums1 and nums2 respectively. Both nums1 and nums2 have the same length. Each encoded1[i] = [vali, freqi] describes the ith segment of nums1, and each encoded2[j] = [valj, freqj] describes the jth segment of nums2.

Return the product of encoded1 and encoded2.

Note: Compression should be done such that the run-length encoded array has the minimum possible length.

 

Example 1:

Input: encoded1 = [[1,3],[2,3]], encoded2 = [[6,3],[3,3]]
Output: [[6,6]]
Explanation: encoded1 expands to [1,1,1,2,2,2] and encoded2 expands to [6,6,6,3,3,3].
prodNums = [6,6,6,6,6,6], which is compressed into the run-length encoded array [[6,6]].
Example 2:

Input: encoded1 = [[1,3],[2,1],[3,2]], encoded2 = [[2,3],[3,3]]
Output: [[2,3],[6,1],[9,2]]
Explanation: encoded1 expands to [1,1,1,2,3,3] and encoded2 expands to [2,2,2,3,3,3].
prodNums = [2,2,2,6,9,9], which is compressed into the run-length encoded array [[2,3],[6,1],[9,2]].
'''


Explanation
A very straightforward solution is to
Expand result for encoded1 (O(10^5) * O(10^4) = O(10^9))
Expand result for encoded2
Calculate product of two results
Use two pointer to get the final result
Well, the issue of above solution, it will get a TLE (Time Limit Exceeded) error. O(10^9) is a time complexity even O(N) solution will get TLE. Thus, we need to do better.
A better solution, instead of expanding the encoded arrays, we can
Take 2 points on each array
Each iteration, take the shorter frequency, calculate product and add to ans
Don't forget to deduct current frequency by the smaller frequency (since it's used), and increment pointers i or j when current frequency is empty
Also, handle the situation where current product is same as the previous product
The time complexity of the above solution is O(10^5), the significance of the length of the encoded array
In the following implementation:
i: Pointer of encoded1
j: Pointer of encoded2
v1: Current value from encoded1[i]
v2: Current value from encoded2[j]
f1: Current frequency of v1
f2: Current frequency of v2
Implementation
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i = j = f1 = f2 = v1 = v2 = 0                # Declare variables
        m, n, ans = len(encoded1), len(encoded2), []
        while i < m or j < n:                        # Starting two pointers while loop
            if not f1 and i < m:                     # If `f1 == 0`, assign new value and frequency
                v1, f1 = encoded1[i]
            if not f2 and j < n:                     # If `f2 == 0`, assign new value and frequency
                v2, f2 = encoded2[j]
            cur_min, product = min(f1, f2), v1 * v2  # Calculate smaller frequency and product
            if ans and ans[-1][0] == product:        # If current product is the same as previous one, update previous frequency
                ans[-1][1] += cur_min
            else:                                    # Other situation, append new pairs
                ans.append([product, cur_min])
            f1 -= cur_min                            # Deduct frequency by smaller frequency (used in current round)
            f2 -= cur_min
            i += not f1                              # When frequency is zero, increment pointer by 1
            j += not f2
        return ans
      
      
-----------------------------------------------------------------------------------     


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0 
        while i < len(encoded1) and j < len(encoded2): 
            val = encoded1[i][0] * encoded2[j][0]
            freq = min(encoded1[i][1], encoded2[j][1])
            if ans and ans[-1][0] == val: ans[-1][1] += freq
            else: ans.append([val, freq])
            encoded1[i][1] -= freq
            encoded2[j][1] -= freq
            if encoded1[i][1] == 0: i += 1
            if encoded2[j][1] == 0: j += 1
        return ans 
---------------------------------------------------------
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        idx1 = 0
        idx2 = 0
        res = []
        
        while idx1<len(encoded1) or idx2<len(encoded2):
            if idx1<len(encoded1) and idx2<len(encoded2):
                min_freq = min(encoded1[idx1][1], encoded2[idx2][1])
                mul = encoded1[idx1][0]*encoded2[idx2][0]
                if min_freq == encoded1[idx1][1]:
                    idx1 += 1
                else:
                    encoded1[idx1][1] -= min_freq
                if min_freq == encoded2[idx2][1]:
                    idx2 += 1
                else:
                    encoded2[idx2][1] -= min_freq
            elif idx1<len(encoded1):
                min_freq = encoded1[idx1][1]
                mul = encoded1[idx1][0]
                idx1 += 1
            else:
                min_freq = encoded2[idx2][1]
                mul = encoded2[idx2][0]
                idx2 += 1
            
            if len(res)>0 and mul == res[-1][0]:
                res[-1][1] += min_freq
            else:
                res.append([mul, min_freq])
        return res
---------------------------------------------------

class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        
        # ans = [[0, 0]]
        ans = []
        ptr1 = 0
        ptr2 = 0
        
        while ptr1 < len(encoded1) and ptr2 < len(encoded2):
            
            elem1, freq1 = encoded1[ptr1]
            elem2, freq2 = encoded2[ptr2]
            
            if freq2 > freq1:
                diff = freq2-freq1
                prod = elem1*elem2
                
                if ans and ans[-1][0] == prod:
                    ans[-1][-1] += freq1
                else:
                    temp = []
                    temp.append(prod)
                    temp.append(freq1)
                    ans.append(temp[:])
                
                encoded2[ptr2][1] = diff
                ptr1 += 1
            
            elif freq1 > freq2:
                diff = freq1-freq2
                prod = elem1*elem2
                
                if ans and ans[-1][0] == prod:
                    ans[-1][-1] += freq2
                else:
                    temp = []
                    temp.append(prod)
                    temp.append(freq2)
                    ans.append(temp[:])
                
                encoded1[ptr1][1] = diff
                ptr2 += 1
            else:
                # diff = freq1-freq2
                prod = elem1*elem2
                
                if ans and ans[-1][0] == prod:
                    ans[-1][-1] += freq1
                else:
                    temp = []
                    temp.append(prod)
                    temp.append(freq1)
                    ans.append(temp[:])
                
                # endcoded1[ptr2][1] = diff
                ptr2 += 1
                ptr1 += 1
        
        return ans
        # return ans[1:]
-------------------------------------------------------

 def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        index1 = 0
        index2 = 0
        
        result = []
        
        while index1 < len(encoded1) and index2 < len(encoded2):
            val1, freq1 = encoded1[index1]
            val2, freq2 = encoded2[index2]
            
            product = val1 * val2
            product_freq = min(freq1, freq2)
            
            if not result or result[-1][0] != product:
                result.append([product, product_freq])
            else:
                result[-1][1] += product_freq
            
            encoded1[index1][1] -= product_freq
            encoded2[index2][1] -= product_freq
            
            index1 += 1 if product_freq == freq1 else 0
            index2 += 1 if product_freq == freq2 else 0
        
        return result
      
---------------------------------------------------------


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        q = deque()
        
        n1, n2 = len(encoded1), len(encoded2)
        i = j = 0
        f1 = f2 = 0
        
        while (i < n1 and j < n2) or f1 or f2:
            if f1 == 0:
                v1, f1 = encoded1[i]
                i += 1
            
            if f2 == 0:
                v2, f2 = encoded2[j]
                j += 1
            
            f = min(f1, f2)
            if q and v1 * v2 == q[-1][0]:
                q[-1][1] += f
            else:
                q.append([v1 * v2, f])
            
            f1 = f1 - f
            f2 = f2 - f
        
        return list(q)

        
      

      
