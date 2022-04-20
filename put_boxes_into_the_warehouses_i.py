'''
You are given two arrays of positive integers, boxes and warehouse, representing the heights of some boxes of unit width and the heights of n rooms in a warehouse respectively. The warehouse's rooms are labelled from 0 to n - 1 from left to right where warehouse[i] (0-indexed) is the height of the ith room.

Boxes are put into the warehouse by the following rules:

Boxes cannot be stacked.
You can rearrange the insertion order of the boxes.
Boxes can only be pushed into the warehouse from left to right only.
If the height of some room in the warehouse is less than the height of a box, then that box and all other boxes behind it will be stopped before that room.
Return the maximum number of boxes you can put into the warehouse.
'''


Algo
Loop through boxes from the largest one to smallest one. If the current box fit in the current room, update counter.

Implementation

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        k = 0
        for box in sorted(boxes, reverse=True): 
            if k < len(warehouse) and box <= warehouse[k]: 
                k += 1
        return k
      
-----------------------------------------------------

Idea
First, find a min prefix for the warehouse. Because the heights in a warehouse are accessible only in non-increasing order.
Then, sort the boxes in the reverse order by their height and try to continuously put the biggest box to the room closest to the entrance.

def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
	aggmin = accumulate(warehouse, min)
	boxes.sort(reverse=True)
	j = fitted = 0
	for h in aggmin:
		while j < len(boxes) and boxes[j] > h: 
			j += 1
		if j >= len(boxes): break
		fitted += 1
		j += 1
	return fitted
-----------------------------------------------

The largest box that a warehouse room can hold is based on its height and the height of all the rooms to its left. Using this information, we can remove any boxes that we know for sure wouldn't fit in the current room or any rooms after it.

Steps:

Sort the boxes in ascending order.
Start on the warehouse room on the far left. For each room (and while we have boxes to insert):
a) Update the running minimum of room heights. This height represents the largest box that could fit into this room. We can also be confident that any rooms to the right of the current room cannot fit boxes larger than this number.
b) While the top of the stack is greater than the running minimum, pop the stack.
c) If there are still boxes remaining, "insert" the largest box we have into the room.
Return the number of boxes inserted
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()
        currMin = float('inf')
        currRoom = 0
        insertedBoxes = 0
        while boxes and currRoom < len(warehouse):
            currMin = min(currMin, warehouse[currRoom])
            # Removing boxes that won't fit anymore
            while boxes and boxes[-1] > currMin:
                boxes.pop()
            if boxes:
                # "Inserting" the box into the current room
                boxes.pop()
                insertedBoxes += 1
            currRoom += 1
        return insertedBoxes
-------------------------------------------------------------

The idea is to create min_allowed_box list for warehouse in which, min_allowed_box[i] = min_found_so_far
For Eg, if warehouse is [5, 3, 3, 4, 1] corresponding min_allowed_box is [5, 3, 3, 3, 1]
Now use Two Pointers to compare each element in both the lists boxes and min_allowed_box and increment the count if boxes[p] <= min_allowed_box[q]

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort() # sort the boxes
        min_allowed_box = []
        min_so_far = float('inf')
        for i in range(len(warehouse)):
            if min_so_far > warehouse[i]:
                min_so_far = warehouse[i]
            min_allowed_box.append(min_so_far)
			
	    # min_allowed_box is [5,3,3,31] for warehouse [5,3,3,4,1].
		# To compare boxes and min_allowed_box, we need to make  min_allowed_box in ascending order as well
        min_allowed_box.reverse()
        
		p, q, count = 0, 0, 0
		
		# two pointers copmare
        while p < len(boxes) and q < len(min_allowed_box):
            if boxes[p] <= min_allowed_box[q]:
                count += 1
                p += 1
            q += 1
        return count
      
      
