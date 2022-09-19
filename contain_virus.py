'''
A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

The world is modeled as an m x n binary grid isInfected, where isInfected[i][j] == 0 represents uninfected cells, and isInfected[i][j] == 1 represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.

Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region (i.e., the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night). There will never be a tie.

Return the number of walls used to quarantine all the infected regions. If the world will become fully infected, return the number of walls used.
'''


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        ans = 0 
        while True: 
            regions = []
            fronts = []
            walls = []
            seen = set()
            for i in range(m): 
                for j in range(n): 
                    if isInfected[i][j] == 1 and (i, j) not in seen: 
                        seen.add((i, j))
                        stack = [(i, j)]
                        regions.append([(i, j)])
                        fronts.append(set())
                        walls.append(0)
                        while stack: 
                            r, c = stack.pop()
                            for rr, cc in (r-1, c), (r, c-1), (r, c+1), (r+1, c): 
                                if 0 <= rr < m and 0 <= cc < n: 
                                    if isInfected[rr][cc] == 1 and (rr, cc) not in seen: 
                                        seen.add((rr, cc))
                                        stack.append((rr, cc))
                                        regions[-1].append((rr, cc))
                                    elif isInfected[rr][cc] == 0: 
                                        fronts[-1].add((rr, cc))
                                        walls[-1] += 1
            if not regions: break
            idx = fronts.index(max(fronts, key = len))
            ans += walls[idx]
            for i, region in enumerate(regions): 
                if i == idx: 
                    for r, c in region: isInfected[r][c] = -1 # mark as quaranteened 
                else: 
                    for r, c in fronts[i]: isInfected[r][c] = 1 # mark as infected 
        return ans 
