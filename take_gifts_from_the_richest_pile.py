'''
You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

Choose the pile with the maximum number of gifts.
If there is more than one pile with the maximum number of gifts, choose any.
Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
Return the number of gifts remaining after k seconds.
'''


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        res = 0
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        while k:

            t = -heapq.heappop(gifts)
            heapq.heappush(gifts, -int(math.floor(math.sqrt(t))))

            k = k-1
        print(gifts)
        gifts = [-g for g in gifts]
        return(sum(gifts))
