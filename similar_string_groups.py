'''
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

 
 '''

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        res = 0
        seen, stack, strs = set(), [], set(strs)
        
        while strs:
            res += 1
            stack.append(strs.pop())
            while stack:
                s = stack.pop()
				# In the first iteration of a new group, we have already removed s from strs in the outer loop by pop.
                if s in strs:
                    strs.remove(s)
                for neigh in strs:
                    if neigh not in seen and len(neigh) == len(s) and self.similar(s,neigh):
                        seen.add(neigh)
                        stack.append(neigh)
        return res
    
    def similar(self,s1,s2):
        diff = 0
        for c1,c2 in zip(s1,s2):
            if c1!=c2:
                diff += 1
        return diff == 2
