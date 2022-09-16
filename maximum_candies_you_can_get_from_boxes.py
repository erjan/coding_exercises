'''
You have n boxes labeled from 0 to n - 1. You are given four arrays: status, candies, keys, and containedBoxes where:

status[i] is 1 if the ith box is open and 0 if the ith box is closed,
candies[i] is the number of candies in the ith box,
keys[i] is a list of the labels of the boxes you can open after opening the ith box.
containedBoxes[i] is a list of the boxes you found inside the ith box.
You are given an integer array initialBoxes that contains the labels of the boxes you initially have. You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.

Return the maximum number of candies you can get following the rules above.

 
 '''


class Solution:
    count = 0  # Found candy. Class variable to keep found candy
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        boxes = []  # Newly found boxes
        progress = False
        for box in initialBoxes:
            if status[box]:  # The box is open
                progress = True
                boxes.extend(containedBoxes[box])  # Add newly found boxes
                self.count += candies[box]  # Count found candy
                for key in keys[box]:
                    status[key] = 1  # Use found keys to open boxes even if we don't have them.
            else:
                boxes.append(box)  # The box is closed. Keep it for the next iteration.
        if not progress:  # Nothing happened. return.
            return self.count
		# Run another iteration with the new 'boxes'
        return self.maxCandies(status, candies, keys, containedBoxes, boxes)
