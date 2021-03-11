'''
ou have a long flowerbed in which some of the plots are planted, and 
some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means
empty and 1 means not empty, and an integer n, return if n new flowers can be planted in 
the flowerbed without violating the no-adjacent-flowers rule.
'''


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = flowerbed
        counter = n
        for i in range(len(f)):
            if f[i] == 0:
                prev, nxt = None, None

                if i == 0 or f[i-1] == 0:
                    prev = 0
                else:
                    prev = 1
                if i == len(f)-1 or f[i+1]==0:
                    nxt = 0
                else:
                    nxt = 1
                if prev == 0 and nxt == 0:
                    f[i] = 1
                    counter-=1

        if counter <= 0:
            return True
        else:
            return False
