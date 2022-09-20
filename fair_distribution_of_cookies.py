'''
You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.
'''


class Solution:
    
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        lo = min(cookies)
        hi = sum(cookies) + 1
        
        def can_satisfy(cookies, max_size, childs: int = k) -> bool:
            if childs == 1:
                return sum(cookies) <= max_size
            
            for mask in range(1, 2**len(cookies)):
                total = 0
                rest = []
                for i in range(len(cookies)):
                    if mask & (1 << i):
                        total += cookies[i]
                    else:
                        rest.append(cookies[i])
                if total <= max_size:
                    if can_satisfy(rest, max_size, childs -1):
                        return True
            
            return False
        
        while lo < hi:
            mid = (lo+hi)//2
            if can_satisfy(cookies, mid):
                hi = mid
            else:
                lo = mid+1
        return lo
