'''
You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players 
into n / 2 teams of size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is 
no way to divide the players into teams such that the total skill of each team is equal.
'''



class Solution:
    def dividePlayers(self, S: List[int]) -> int:
        S.sort()
        n = len(S)
        s = S[0] + S[-1]
        total = 0
        for i in range(n // 2):
            if s != S[i] + S[n - i - 1]:
                return -1
            total += S[i] * S[n - i - 1]
            
        return total
      
-----------------------------------------------------------------------------------------------
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        chemistry = 0

        skill.sort()

        l = 0
        r = len(skill)-1

        temp = skill[0] + skill[-1]
      
        n = len(skill)
        while l<r:
            if temp!= skill[l]+skill[r]:
                return -1
            chemistry += skill[l]*skill[r]
            l+=1
            r-=1

        return chemistry
