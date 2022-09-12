'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]
---------------------------------------------------------------------------------------
Standard QuickSelect Algorithm(like QuickSort)
Given a sequence seq and a positive number k, we need to find out the top k elements from seq.
Randomly select a pivot from the current seq
random selection is very important, on average, this can effectively deal with the worst case.
Traverse seq one by one, count how many elements less than or greater than or equal to the pivot respectively.
There are 3 different situations
k <= len(less)
that means you can find all top k elements in less recursively.
len(less) < k <= len(less) + len(equal)
congratulations! pivot is the k-th element, note to handle equal situations carefully.
k > len(less) + len(equal)
Not bad. you have already found the top len(less) + len(equal) elements.
you can find out the left k - len(less) + len(equal) top elements from greater recursively.


class Solution(object):
    def kClosest(self, points, k):
        def quickSelect(points, k):
            less, equal, greater = [], [], []
            pivot = random.choice(points)
            pivot_l2 = pivot[0] ** 2 + pivot[1] ** 2
            for p in points:
                p_l2 = p[0] ** 2 + p[1] ** 2
                if p_l2 < pivot_l2:
                    less.append(p)
                elif p_l2 > pivot_l2:
                    greater.append(p)
                else:
                    equal.append(p)
            if len(less) < k <= len(less) + len(equal):
                return less + equal[:k - len(less)]
            elif k <= len(less):
                return quickSelect(less, k)
            else:
                return less + equal + quickSelect(greater, k - len(less) - len(equal))
				
        return quickSelect(points, k)
