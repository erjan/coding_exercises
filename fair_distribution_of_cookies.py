'''
You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.
'''


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        result = float('inf')
        children = [0] * k
        
        def backtrack(index):
            nonlocal result, children
            
            if index == len(cookies):
                result = min(result, max(children))
                return
				
			# key point to pass the TLE!
            if result <= max(children):
                return
            
            for i in range(k):
                children[i] += cookies[index]
                backtrack(index + 1)
                children[i] -= cookies[index]
                
        backtrack(0)
        
        return result
