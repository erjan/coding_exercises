'''
Given an array of strings words, return the smallest string that contains each string in words as a
substring. If there are multiple valid strings of the smallest length, return any of them.

You may assume that no string in words is a substring of another string in words.
'''
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        graph = [[0]*n for _ in range(n)] # graph as adjacency matrix 
        
        for i in range(n):
            for j in range(n): 
                if i != j: 
                    for k in range(len(words[j])): 
                        if words[i].endswith(words[j][:k]): 
                            graph[i][j] = len(words[j]) - k 
                            
        @cache
        def fn(prev, mask): 
            """Return length of shortest superstring & current choice of word."""
            if mask == 0: return 0, None
            vv, kk = inf, None
            for k in range(n): 
                if mask & 1<<k: 
                    v, _ = fn(k, mask ^ 1<<k)
                    offset = len(words[k]) if prev == -1 else graph[prev][k]
                    if v + offset < vv: vv, kk = v + offset, k
            return vv, kk
        
        ans = []
        prev = -1 
        mask = (1<<n) - 1
        while mask: 
            _, k = fn(prev, mask)
            if ans: ans.append(words[k][-graph[prev][k]:])
            else: ans.append(words[k])
            prev = k
            mask ^= 1<<k 
        return "".join(ans)

