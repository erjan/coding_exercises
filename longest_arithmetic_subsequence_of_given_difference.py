'''
Given an integer array arr and an integer difference, return the 
length of the longest subsequence in arr which is an arithmetic sequence such that 
the difference between adjacent elements in the subsequence equals difference.

A subsequence is a sequence that can be derived from
arr by deleting some or no elements without changing the order of the remaining elements.
'''


In map/dictionary we keep track of the number and the length of the series till that number.
Assuming my current number is 7 and K = -2, then I will look in the map if I can find 
9, if  yes then I know that my longest length till now = length till 9 + 1(for current number 7)

As I am starting from the 0th index, so when I see a number 7, I will look if I can find a
number 9 before 7, so that I can make a subsequence, 9, 7, etc.

 def longestSubsequence(self, arr: List[int], difference: int) -> int:
    dic = {}
    res = float('-inf')
    for num in arr:
        count = 1
        if num - difference in dic:
            count += dic[num - difference]
        
        dic[num] = count
        
        res = max(res, dic[num])
    
    return res
  
-------------------------------------------------------------------------------------------------------------------------
'''
Intuition
This is a little bit different than regular dp problems, we use hash table instead of arrays for dp table.
For given number in the input array x, we want to find if x-d exists before x:
If x-d exists, then it means that x-d can be extended with x, thus the longest subsequence up to x is dp[x-d] + 1, which means dp[x] = dp[x-1] + 1
Else if x-d does not exists before x (never seen before x), x is the first element in potential sequence, so dp[x] = 1
After iterating all elements in input array, we pick the largest value in the hash table.

'''


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
        dp is a hashtable, dp[x] is the longest subsequence ending with number x
        """
        dp = {}
        for x in arr:
            if x - difference in dp:
                dp[x] = dp[x-difference] + 1
            else:
                dp[x] = 1
            
        return max(dp.values())
