'''
You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array persons of size n, where persons[i] is the time that the ith person will arrive to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.
'''

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        start, end, res = [], [], []
        for i in flowers:
            start.append(i[0])
            end.append(i[1])
        start.sort() #bisect only works with sorted data
        end.sort()

        for p in persons:
            num = bisect_right(start, p) - bisect_left(end, p)
            res.append(num)
        return res
#bisect_right(start, p) gives you the number of flowers that are in full bloom at person p.
#bisect_left(end, p) gives you number of flowers that are not in full bloom at person p.
#we have to tighten our bound to get exact number of flowers that are in bloom or not, thats why we are using right and left of bisect module.

-------------------------------------------------------------------------------------------------------
from heapq import heappush, heappop

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        out = [0 for _ in range(len(persons))]
        persons = [(arrival, i) for i, arrival in enumerate(persons)]
        persons.sort()
        flowers.sort()

        heap = []
        f_idx = 0
        for arrival, person_idx in persons:
            while f_idx < len(flowers) and flowers[f_idx][0] <= arrival:
                heappush(heap, flowers[f_idx][1])
                f_idx += 1
            while len(heap) and heap[0] < arrival:
                heappop(heap)
            out[person_idx] = len(heap)
        return out
