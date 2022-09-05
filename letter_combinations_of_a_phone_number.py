'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        s = dict()
        s[2] = 'abc'
        s[3] = 'def'
        s[4] = 'ghi'
        s[5] = 'jkl'
        s[6] = 'mno'
        s[7] = 'pqrs'
        s[8] = 'tuv'
        s[9] = 'wxyz'

        temp = list()

        for d in digits:
            temp.append(s[int(d)])

        res = list(map("".join, product(*(s[int(k)] for k in digits))))
        print(res)
        return res
        
------------------------------------------------------------------------------------------------------------ 

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        res=[]
        if len(digits) ==0:
            return res
            
        self.dfs(digits, 0, dic, '', res)
        return res
    
    def dfs(self, nums, index, dic, path, res):
        if index >=len(nums):
            res.append(path)
            return
        string1 =dic[nums[index]]
        for i in string1:
            self.dfs(nums, index+1, dic, path + i, res)
-------------------------------------------------------------------
def subsets(self, nums):
    def backtrack(start, end, tmp):
        ans.append(tmp[:])
        for i in range(start, end):
            tmp.append(nums[i])
            backtrack(i+1, end, tmp)
            tmp.pop()
    ans = []
    backtrack(0, len(nums), [])
    return ans
