'''
In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.
'''


def rearrangeBarcodes(barcodes):

	# Our result to return
	result = []
	
	# Get the counts
	counts = collections.Counter(barcodes)
	
	# Create a max-heap based on count
	heap = [[-v, k] for k, v in counts.items()]
	
	# Heapify the heap
	heapq.heapify(heap)
	
	# Get the first item
	item = heapq.heappop(heap)

	while heap:
		result.append(item[1])
		item[0] += 1 # "Decrease" the count (remember our count is negative for min-heap, that's why we add)
		
		"""
		'heapreplace' will pop the next item onto the heap, then push the old item!
		Its the secret weapon for this solution.
		We heappop if we don't want to push 'item' back onto the heap.
		"""
		item = heapq.heapreplace(heap, [item[0], item[-1]]) if item[0] < 0 else heapq.heappop(heap)

	# Because I do a `heappop` outside of the while loop, we should append the last element!
	result.append(item[1])

	return result
--------------------------------------------------------------------------------------
class Solution:
    def rearrangeBarcodes(self, barcodes):
        count, pq, ans = {}, [], []
        for num in barcodes:
            try: 
                count[num] += 1
            except:
                count[num] = 1
        for n, c in count.items():
            heapq.heappush(pq, (-c, n))
        prev_cnt, prev_num = 0, 0
        while pq:
            cnt, num = heapq.heappop(pq)
            if prev_cnt:
                heapq.heappush(pq, (prev_cnt, prev_num))
            ans.append(num)
            prev_cnt, prev_num = cnt+1, num
        return ans
