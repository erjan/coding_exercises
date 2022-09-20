'''
You are given an integer array matchsticks where matchsticks[i] is the length of 
the ith matchstick. You want to use all the matchsticks to make one square. You should not break any 
stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

'''

---------------------------------------------------------------------------------------
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        value = sum(matchsticks)
        if value < 4:
            return False
        if value % 4 != 0:
            return False
        
        target = sum(matchsticks)//4
        
        
        matchsticks.sort(reverse=True)
        
                                        
        @cache
        def backtrack(a,b,c,d, i ):
            nonlocal target

            if a == b==c==d==target:
                return True
            
            if i > len(matchsticks)-1:
                return False
            
            if a > target or b > target or c > target or d > target:
                return False
            
            cur_stick = matchsticks[i]
            return backtrack(a+cur_stick,b,c,d,i+1) or \
                        backtrack(a,b+cur_stick,c,d,i+1) or \
                        backtrack(a,b,c+cur_stick,d,i+1) or \
                        backtrack(a,b,c,cur_stick+d,i+1)
        
        return backtrack(0,0,0,0,0)



-----------------------------------------------------------------------------------------------------------------    
    
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        value = sum(matchsticks)
        if value < 4:
            return False
        if value % 4 != 0:
            return False
        edge = value // 4
        matchsticks.sort(reverse=True)
        @cache
        def findedges(l1, l2, l3, l4, i):
            nonlocal edge
            if l1 == l2 == l3 == l4 == edge:
                return True
            if i > len(matchsticks) - 1:
                return False
            if l1 > edge or l2 > edge or l3 > edge or l4 > edge:
                return False
            return findedges(l1 + matchsticks[i], l2, l3, l4, i + 1) or findedges(l1, l2 + matchsticks[i] , l3, l4, i + 1) or findedges(l1, l2, l3 + matchsticks[i], l4, i + 1) or findedges(l1, l2, l3, l4 + matchsticks[i] , i + 1)
        return findedges(0, 0, 0, 0, 0)
