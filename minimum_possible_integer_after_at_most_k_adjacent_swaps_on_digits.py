'''
You are given a string num representing the digits of a very large integer and an integer k. You are allowed to swap any two adjacent digits of the integer at most k times.

Return the minimum integer you can obtain also as a string.
'''

from bisect import bisect


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        len_num = len(num)
        if k >= len_num * (len_num - 1) / 2:
            return ''.join(sorted(num))
        pos = [[] for _ in range(10)]
        for i in range(len_num - 1, -1, -1):
            pos[int(num[i])].append(i)
        prev = []
        ans = ''
        candi = list(range(10))
        while k and len(ans) < len_num:
            for di in candi[:]:
                if pos[di]:
                    index = pos[di][-1]
                    place = bisect(prev, index)
                    if index - place <= k:
                        prev.insert(place, index)
                        k -= index - place
                        pos[di].pop()
                        ans += str(di)
                        break
                else:
                    candi.remove(di)
        if k == 0 and len(ans) < len_num:
            prev = set(prev)
            return ans + ''.join(ch for i, ch in enumerate(num) if i not in prev)
        else:
            return ans
--------------------------------------------------------------------------------------------------------
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        if k >= n*(n-1)//2: return "".join(sorted(num)) #special case
        
        #find smallest elements within k swaps 
        #and swap it to current position 
        num = list(num)
        for i in range(n):
            if not k: break 
            #find minimum within k swaps
            ii = i
            for j in range(i+1, min(n, i+k+1)): 
                if num[ii] > num[j]: ii = j 
            #swap the min to current position 
            if ii != i: 
                k -= ii-i
                for j in range(ii, i, -1):
                    num[j-1], num[j] = num[j], num[j-1]
        return "".join(num)
