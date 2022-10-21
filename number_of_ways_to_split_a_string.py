'''
Given a binary string s, you can split s into 3 non-empty strings s1, s2, and s3 where s1 + s2 + s3 = s.

Return the number of ways s can be split such that 
the number of ones is the same in s1, s2, and s3. Since the answer may be too large, return it modulo 109 + 7.
'''

from math import comb
class Solution:

def numWays(self, s: str) -> int:
    count = s.count("1")
    ans = [0, 0]
    if count%3 != 0:
        return 0
    elif count == 0: # string with len(s) has len(s)-1 intervals, you can choose any two to divide the string
        return comb(len(s)-1,2)%(10**9+7)
    left = 0
    right = len(s)-1
    cum_s = 0
    cum_e = 0
    while(cum_s<=count//3 or cum_e<=count//3):
        if s[left] == "1":
            cum_s+=1
        if s[right] == "1":
            cum_e+=1
        if cum_s == count//3: # from index 0, count how many different substrings have count//3 "1"
            ans[0]+=1
        if cum_e == count//3: # from index len(s)-1, count how many different substrings have count//3 "1"
            ans[1]+=1
        left+=1
        right-=1 
    return (ans[0]*ans[1])%(10**9+7)
  
------------------------------------------------------------------------------------------------------------------------------------------  
class Solution:
    def numWays(self, s: str) -> int:
        n = s.count('1')
        if n and n % 3:
            return 0
        if not n:
            return math.comb(len(s)-1, 2) % 1_000_000_007
        ans, count, prev = 1, 0, -1
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
                if (count - 1) * 3 == n or (count - 1) * 3 == n * 2:
                    ans *= i - prev
                prev = i    
        return ans % 1_000_000_007 
      
------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def numWays(self, s: str) -> int:

        
        memo = {}
        def backTracking(curr_path, s, count):
            if (len(s), count) in memo:
                return memo[(len(s), count)]
            if not s:
                if count == 3:
                    return 1
                return 0

            res = 0
            for i in range(1, len(s) + 1):
                sub_string = s[0 : i]
                if curr_path == None:
                    res += backTracking(sub_string.count("1"), s[i : ], count + 1)
                else:
                    if sub_string.count("1") == curr_path:
                        res += backTracking(sub_string.count("1"), s[i : ], count + 1)
                    else:
                        continue
            memo[(len(s), count)] = res
            return memo[(len(s), count)]
        L = backTracking(None, s, 0)
        return L
----------------------------------------------------------------------------------------------------------
class Solution:
    modulo = pow(10, 9) + 7

    def numWays(self, s: str) -> int:
        ones = s.count("1")
        if ones and not ones % 3:
            target = ones // 3
            target1 = target + 1
            double_target = 2 * target
            double_target1 = double_target + 1
            ones_count = 0
            end_part1 = start_part2 = end_part2 = start_part3 = 0
            for i, c in enumerate(s):
                if c == "1":
                    ones_count += 1
                    if ones_count == target:
                        end_part1 = i
                    if ones_count == target1:
                        start_part2 = i
                    if ones_count == double_target:
                        end_part2 = i
                    if ones_count == double_target1:
                        start_part3 = i
                        break
            return ((start_part2 - end_part1) * (start_part3 - end_part2)
                    % Solution.modulo)
        elif not ones and len(s) > 2:
            k = len(s) - 2
            return k * (1 + k) // 2 % Solution.modulo
        return 0
      
---------------------------------------------------------------------------------------------------------------

'''
We can divide given problem in 2 ways

Number of "1"(ones) present in string is not a multiple of 3
----> If this is the case means we cannot divide simply return 0
Number of "1"(ones) present in string is a multiple of 3
----> There can be also 2 possible cases , when count of "1"s is zero and when count of "1"s is not zero.
If count of "1"s is zero , imagine this case as we have n-1 places(indexes) to choose and we have to select only 2 places(indexes) to partition into three non empty strings, means answer will be (n-1)C2
i.e. ((n-1)*(n-2))/2
If count of "1"s is non zero , find out four indexes:
first calculate -> count of all ones/3 which is number of ones that should be present in a partition.
indx1 = right most index in first partitioned string which is "1"
indx2 = left most index in third partioned string which is "1"
indx3 = left most index in second partioned string which is "1"
indx4 = right most index in second partioned string which is "1"
At end simply multiply their differences.
'''


      
