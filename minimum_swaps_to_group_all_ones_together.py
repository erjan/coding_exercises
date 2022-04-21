'''
Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

 

Example 1:

Input: data = [1,0,1,0,1]
Output: 1
Explanation: There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
Example 2:

Input: data = [0,0,0,1,0]
Output: 0
Explanation: Since there is only one 1 in the array, no swaps are needed.
Example 3:

Input: data = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
'''

def minSwaps(self, data: List[int]) -> int:
	"""
	This is a classic sliding window problem. We maintain two pointers, left and right.
	1. Calculate the total number of ones in the array
	2. Initialize left and right as 0
	3. Now iterate the right pointer and at each point add to count of ones if the item is 1
	4. While doing this, if (r - l + 1, which is number of elements in the window) ever exceeds the 
	total number of ones, then we have to move left pointer as well. In this case before moving, subtract
	from count of ones, the value of the current left pointer position.
	5. Update max number of ones found at each stage.
	6. Now finally the total number of swaps will be the difference between total ones and the max number of ones found so far.
	"""
	size = len(data)
	total_ones = sum(data)

	l = curr_ones_in_window = max_ones_seen_so_far = 0

	for r in range(size):
		curr_ones_in_window+=data[r]

		if r - l + 1 > total_ones:
			curr_ones_in_window-=data[l]
			l+=1

		max_ones_seen_so_far = max(max_ones_seen_so_far, curr_ones_in_window)

	return total_ones - max_ones_seen_so_far

-------------------------------------------------

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        k = sum(data) # window size 
        ans = val = 0 
        for i, x in enumerate(data): 
            val += x
            if i >= k: val -= data[i-k]
            if i+1 >= k: ans = max(ans, val)
        return k - ans
      
      
------------------------------------------------------------------------------------
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # Number of ones
        window = 0
        
        # Count ones
        for d in data:
            window += d
            
        # Main part
        current_ones, max_ones = 0, 0
        
        for i in range(len(data)):
            current_ones += data[i]
            
            # If the right pointer passes the window, update the left pointer
            # Also, if add too many, subtract
            if i >= window:
                current_ones -= data[i - window]
                
            # Update max so far
            max_ones = max(current_ones, max_ones)
        
        return window - max_ones
-------------------------------------------------------

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # COUNT THE TOTAL NUMBER OF ONES
        totalOnes = sum(data)
        # INITIALISE FIRST WINDOW SUM
        initialSum = sum(data[: totalOnes])
        minVal = totalOnes - initialSum
        
        for index in range(1, len(data) - totalOnes + 1):
            # UPDATE THE WINDOW SUM BY SUBTRACTING LEFT EXTREME AND ADDING RIGHT EXTREME
            initialSum = initialSum - data[index - 1] + data[index + totalOnes - 1]
            # NUMBER OF SWAPS REQUIRED IS THE DIFFERENCE BETWEEN TOTAL ONES AND COUNT OF ONES IN CURRENT WINDOW
            swaps = totalOnes - initialSum
            
            # UPDATE MINSWAPS
            if swaps < minVal:
                minVal = swaps
                
        return minVal
--------------------------------------------------------------------------------

   def minSwaps(self, data: List[int]) -> int:
        number_ones = sum(data)
        max_num_ones = current = sum(data[:number_ones])

        for left, right in zip(data, data[number_ones:]):
            current += right
            current -= left
            max_num_ones = max(max_num_ones, current)

        return(number_ones - max_num_ones)
-------------------------------------------------

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        cnt_1=data.count(1)
        if cnt_1==1: return 0
        if cnt_1==0: return 0
        
        cnt_2=data[0:0+cnt_1].count(1)
        slt=cnt_1-cnt_2
        
        for i in range(cnt_1,len(data)):
            if data[i]==1 and data[i-cnt_1]==1:
                continue
            if data[i]==1 and data[i-cnt_1]==0:
                cnt_2+=1
            if data[i]==0 and data[i-cnt_1]==0:
                continue
            if data[i]==0 and data[i-cnt_1]==1:
                cnt_2-=1
            slt=min(slt,cnt_1-cnt_2)
        return slt
      
      
      
      
