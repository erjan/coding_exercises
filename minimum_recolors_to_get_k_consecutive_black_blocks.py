'''
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.
'''


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        s = blocks
        res = float('inf')

        if len(s) == k:
            return min(res, len(s) - s.count('B') )
        
        for i in range(len(s)-k+1):
            temp = s[i:i+k]
            b = temp.count('B')

            t = len(temp) - b

            res = min(res, t)
            print(temp)
        print(res)
        return res
