'''
In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.

It is guaranteed an answer exists.
'''


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        mp = {skill : i for i, skill in enumerate(req_skills)} # digitized skills
        
        cand = []
        for skills in people: 
            val = 0
            for skill in skills: 
                val |= 1 << mp[skill] # digitized skill
            cand.append(val)
        
        @cache
        def fn(i, mask): 
            """Return smallest sufficient team of people[i:] for skills in mask."""
            if mask == 0: return []
            if i == len(people): return [0]*100 # impossible
            if not (mask & cand[i]): return fn(i+1, mask)
            return min(fn(i+1, mask), [i] + fn(i+1, mask & ~cand[i]), key=len)
        
        return fn(0, (1 << len(req_skills)) - 1)
      
-----------------------------------------------------------------------------------------------------------------
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        res = [''] * 17
        n = len(req_skills)
        def dfs(idx, has, path):
            nonlocal res
            if idx == n:
                res = path
            elif req_skills[idx] in has:
                dfs(idx + 1, has, path)
            else:
                if len(path) + 1 < len(res):
                    for i, p in enumerate(people):
                        p = set(p)
                        if req_skills[idx] in p:
                            union = p & has
                            has |= p
                            dfs(idx + 1, has, path + [i])
                            has -= p
                            has |= union
        dfs(0, set(), [])
        return res
		
