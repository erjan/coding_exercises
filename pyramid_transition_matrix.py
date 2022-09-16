'''
You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains one less block than the row beneath it and is centered on top.

To make the pyramid aesthetically pleasing, there are only specific triangular patterns that are allowed. A triangular pattern consists of a single block stacked on top of two blocks. The patterns are given as a list of three-letter strings allowed, where the first two characters of a pattern represent the left and right bottom blocks respectively, and the third character is the top block.

For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of an 'A' (left) and 'B' (right) block. Note that this is different from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom.
You start with a bottom row of blocks bottom, given as a single string, that you must use as the base of the pyramid.

Given bottom and allowed, return true if you can build the pyramid all the way to the top such that every triangular pattern in the pyramid is in allowed, or false otherwise.

'''

class Solution(object):

    def pyramidTransition(self, bottom, allowed):
        f = collections.defaultdict(lambda: defaultdict(list))
        for a, b, c in allowed: f[a][b].append(c)

        def pyramid(bottom):
            if len(bottom) == 1: return True
            for i in itertools.product(*(f[a][b] for a, b in zip(bottom, bottom[1:]))):
                if pyramid(i): return True
            return False
        return pyramid(bottom)
      
------------------------------------------------------------

class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        self.mapping = collections.defaultdict(set)
        for brick in allowed:
            self.mapping[brick[:2]].add(brick[2])
            
        cur_level, cur_len = bottom, len(bottom)
        return self.search(cur_level, cur_len)
                    
                    
    def search(self, cur_level, cur_len):
        if cur_len == 1:
            return True
        
        next_cand = ' '        
        for i in range(cur_len-1):
            if cur_level[i:i+2] in self.mapping:
                next_cand = map(''.join, itertools.product(next_cand, self.mapping[cur_level[i:i+2]]))
            else:
                return False
            
        if next_cand: 
            for cand in list(next_cand):
                if self.search(cand[1:], cur_len-1):
                    return True
        return False
