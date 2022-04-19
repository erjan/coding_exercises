'''
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate 
the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.
'''


As we cannot pick the two elements from the same array, we just calculate the distance between the current min/max with the previous min/max.

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mn, mx = arrays[0][0], arrays[0][-1]
        diff = -float("inf")
        for ar in arrays[1:]:
            mx_diff = abs(mx - ar[0])
            mn_diff = abs(mn - ar[-1])
            diff = max(diff, mn_diff, mx_diff)
            if ar[0] < mn:
                mn = ar[0]
            if ar[-1] > mx:
                mx = ar[-1]
        return diff
      
-----------------------------------------------------------


First, we save the minimum of each array into min_num dictionary as key and save the maximum of each array into max_num dictionary as key.
Second, we compare the distance and find the maximum distance.
Third, the key point is the max and min should not come from the same string. We take two steps to avoid this situation: save the array index as the value list, that's why we define the dictionary value as list type :) ; check whether the list are the same or the length of the list larger than 1. In this way, we can make sure that the max and min are not from the same array.

def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        min_num=collections.defaultdict(list)
        max_num=collections.defaultdict(list)
        i=0
        distance=0
        for array in arrays:
            min_num[array[0]].append(i)
            max_num[array[-1]].append(i)
            i+=1
        for i in min_num:
            for j in max_num:
                if (j-i)>distance:
                    if min_num[i]!=max_num[j]:
                        distance=j-i
                    elif len(min_num[i])>1:
                        distance=j-i
        return distance
---------------------------------------------


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        cur_min = arrays[0][0]
        cur_max = arrays[0][-1]
        cur_dist = 0
        for arr in arrays[1:]:
            cur_dist = max(cur_dist, abs(arr[-1] - cur_min), abs(cur_max - arr[0]))
            cur_min = min(cur_min, arr[0])
            cur_max = max(cur_max, arr[-1])
        return cur_dist
      
----------------------------------------------

I wonder if in an interview setting under pressure all those other cute solutions do actually come to mind. Anyway, since the hope is to get the optimal solution which should be O(N) and keep the memory consumption to O(1), one would try to find the biggest maximum and the smallest minimum, which can be done in a single pass. Then, if these two happen to belong to the same list, we do another pass and find the second maximum/minimum and return the result. I think this thought process is more realistic in a real interview where there's pressure.

def maxDistance(self, arrays: List[List[int]]) -> int:
	minidx = maxidx = 0

	for i, val in enumerate(arrays):
		if val[0] < arrays[minidx][0]: minidx = i
		if val[-1] > arrays[maxidx][-1]: maxidx = i

	if minidx != maxidx: return abs(arrays[maxidx][-1] - arrays[minidx][0])

	# overlap, let's do another pass
	twominidx = twomaxidx = (maxidx + 1) % len(arrays)
	for i, val in enumerate(arrays):
		if i == maxidx: continue
		if val[0] < arrays[twominidx][0]: twominidx = i
		if val[-1] > arrays[twomaxidx][-1]: twomaxidx = i

	return max(abs(arrays[twomaxidx][-1] - arrays[minidx][0]), abs(arrays[maxidx][-1] - arrays[twominidx][0]))
---------------------------------------------

The most straightforward and the fastest (between provided in this post) solution


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_first = math.inf
        max_last = -math.inf
        min_idx = None
        max_idx = None
        
        get_first_last_elements = itemgetter(0, -1)
        first_last_elems = map(get_first_last_elements, arrays)
        
        for i, (first_elem, last_elem) in enumerate(first_last_elems):
            if first_elem < min_first:
                min_first = first_elem
                min_idx = i
            
            if last_elem > max_last:
                max_last = last_elem
                max_idx = i
                
        if min_idx != max_idx:
            return abs(max_last - min_first)
        else:
            min_prev_first = math.inf
            max_prev_last = -math.inf
            
            first_last_elems = map(get_first_last_elements, arrays)
            
            for i, (first_elem, last_elem) in enumerate(first_last_elems):
                if first_elem < min_prev_first and i != min_idx:
                    min_prev_first = first_elem

                if last_elem > max_prev_last and i != max_idx:
                    max_prev_last = last_elem
                    
            return max(abs(max_last - min_prev_first),
                       abs(max_prev_last - min_first))
Refactored previous solution


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        get_first_element = itemgetter(0)
        get_last_element = itemgetter(-1)
        
        first_elems = list(map(get_first_element, arrays))
        last_elems = list(map(get_last_element, arrays))
        
        get_element = itemgetter(1)
        min_idx, min_first = min(enumerate(first_elems), key=get_element)        
        max_idx, max_last = max(enumerate(last_elems), key=get_element)
        
        if min_idx != max_idx:
            return abs(max_last - min_first)
        else:
            first_elems.pop(min_idx)
            last_elems.pop(max_idx)
            
            min_prev_idx, min_prev_first = min(enumerate(first_elems), key=get_element)        
            max_prev_idx, max_prev_last = max(enumerate(last_elems), key=get_element)
            return max(abs(max_last - min_prev_first),
                       abs(max_prev_last - min_first))
Solution based on numpy.argpartition

import numpy as np

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        get_first_element = itemgetter(0)
        get_last_element = itemgetter(-1)
        
        first_elems = list(map(get_first_element, arrays))
        last_elems = list(map(get_last_element, arrays))
        
        min_indices = np.argpartition(first_elems, 1)[:2]
        max_indices = np.argpartition(last_elems, -2)[-2:][::-1]
        
        if min_indices[0] != max_indices[0]:
            return abs(last_elems[max_indices[0]] - first_elems[min_indices[0]])
        else:
            return max(abs(last_elems[max_indices[0]] - first_elems[min_indices[1]]),
                       abs(last_elems[max_indices[1]] - first_elems[min_indices[0]]))
Solution based on heap

from operator import itemgetter

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        get_first_element = itemgetter(0)
        get_last_element = itemgetter(-1)
        get_element = itemgetter(1)
        
        arrays_count = len(arrays)
        
        first_elems = dict(zip(range(arrays_count), map(get_first_element, arrays)))
        last_elems = dict(zip(range(arrays_count), map(get_last_element, arrays)))
        
        min_indices = nsmallest(2, first_elems.keys(), key=first_elems.get)
        max_indices = nlargest(2, last_elems.keys(), key=last_elems.get)

        if min_indices[0] != max_indices[0]:
            return abs(last_elems[max_indices[0]] - first_elems[min_indices[0]])
        else:
            return max(abs(last_elems[max_indices[0]] - first_elems[min_indices[1]]),
                       abs(last_elems[max_indices[1]] - first_elems[min_indices[0]]))
Python version of the official solution


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_dist = -math.inf

        min_first = arrays[0][0]
        max_last = arrays[0][-1]
        
        get_first_last_elements = itemgetter(0, -1)
        first_last_elems = map(get_first_last_elements, arrays[1:])
        
        for first_elem, last_elem in first_last_elems:
            max_dist = max(max_dist, 
                           abs(max_last - first_elem), 
                           abs(last_elem - min_first))
            min_first = min(min_first, first_elem)
            max_last = max(max_last, last_elem)   
            
        return max_dist
      
---------------------------------------------
class Solution:
  def maxDistance(self, arrays: List[List[int]]) -> int:
    max_dist = max(
      abs(arrays[0][0] - arrays[1][-1]),
      abs(arrays[0][-1] - arrays[1][0])
    )
    min_val = min(arrays[0][0], arrays[1][0])
    max_val = max(arrays[0][-1], arrays[1][-1])
    
    for idx in range(2, len(arrays)):
      curr_min = arrays[idx][0]
      curr_max = arrays[idx][-1]
      
      dist1 = abs(max_val - curr_min)
      dist2 = abs(curr_max - min_val)
      
      min_val = min(min_val, curr_min)
      max_val = max(max_val, curr_max)
      
      max_dist = max(max_dist, dist1, dist2)
      
    return max_dist
'''
[[1,2,3],[4,5],[1,2,3]]
[[1],[1]]
[[1],[2]]
[[1,4],[0,5]]
[[1,5],[3,4]]
[[1,2,3],[4,5],[1,2,3]]
[[1,4,5],[0,2]]
[[2,8],[5,15]]
[[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]]
'''
      
