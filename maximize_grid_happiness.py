'''
You are given four integers, m, n, introvertsCount, and extrovertsCount. You have an m x n grid, and there are two types of people: introverts and extroverts. There are introvertsCount introverts and extrovertsCount extroverts.

You should decide how many people you want to live in the grid and assign each of them one grid cell. Note that you do not have to have all the people living in the grid.

The happiness of each person is calculated as follows:

Introverts start with 120 happiness and lose 30 happiness for each neighbor (introvert or extrovert).
Extroverts start with 40 happiness and gain 20 happiness for each neighbor (introvert or extrovert).
Neighbors live in the directly adjacent cells north, east, south, and west of a person's cell.

The grid happiness is the sum of each person's happiness. Return the maximum possible grid happiness.

'''

class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        
        @cache
        def fn(prev, i, j, intro, extro): 
            """Return max grid happiness at (i, j)."""
            if i == m: return 0 # no more position
            if j == n: return fn(prev, i+1, 0, intro, extro)
            if intro == extro == 0: return 0 
            
            prev0 = prev[:j] + (0,) + prev[j+1:]
            ans = fn(prev0, i, j+1, intro, extro)
            if intro: 
                val = 120 
                if i and prev[j]: # neighbor from above 
                    val -= 30 
                    if prev[j] == 1: val -= 30 
                    else: val += 20 
                if j and prev[j-1]: # neighbor from left 
                    val -= 30 
                    if prev[j-1] == 1: val -= 30 
                    else: val += 20 
                prev0 = prev[:j] + (1,) + prev[j+1:]
                ans = max(ans, val + fn(prev0, i, j+1, intro-1, extro))
            if extro: 
                val = 40 
                if i and prev[j]: 
                    val += 20 
                    if prev[j] == 1: val -= 30 
                    else: val += 20 
                if j and prev[j-1]: 
                    val += 20 
                    if prev[j-1] == 1: val -= 30 
                    else: val += 20 
                prev0 = prev[:j] + (2,) + prev[j+1:]
                ans = max(ans, val + fn(prev0, i, j+1, intro, extro-1))
            return ans 
        
        return fn((0,)*n, 0, 0, introvertsCount, extrovertsCount)

