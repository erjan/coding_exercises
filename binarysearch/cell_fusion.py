'''
You are given a list of integers cells, representing sizes of different cells. In each iteration, the two largest cells a and b interact according to these rules:

If a = b, they both die.
Otherwise, the two cells merge and their size becomes floor((a + b) / 3).
Return the size of the last cell or return -1 if there's no cell is remaining.
'''


import heapq

class Solution:
    def solve(self, cells):
        

        heap = []
        heapq.heapify(heap)

        for c in cells:

            heapq.heappush(heap, -1*c)
      

        while heap and len(heap) > 1:

            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)


            if a != b:
                q = math.floor((a+b)/3)
                heapq.heappush(heap, -1*q)
            #else:
                #print('a = b so die!')

        if len(heap) == 0:
            return -1
        return -heap[0]
        
---------------------------------------------------------------------
class Solution:
    def solve(self, cells):
        pq = [-cell for cell in cells]
        heapq.heapify(pq)
        while len(pq) > 1:
            a, b = heapq.heappop(pq), heapq.heappop(pq)
            if a != b:
                heapq.heappush(pq, (-a - b) // 3 * -1)
        return -1 if not pq else -pq[0]
