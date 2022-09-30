'''
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.
'''

The most difficult part in this problem, or in all sliding window problems in general, is to come up with some way to find if a particular window is valid or not because if we know that, then any sliding window problem is a piece of cake. Sometimes we are directly given in the problem statement but most of the times we have to figure out some sort of check for a valid subarray.

This particular problem is like that. Yes, we are given the number of moves/increments we can do in a window but how to know if a particular window is valid or not?

Just think about it. We want to make all the numbers the same in any window by doing at most k increments. So we want to efficiently use our moves and for any element, we want to use the least amount of moves possible to turn it into another element.

This means, the element that we want to increment and the element that we want others to turn into, should be as close as possible. In short, the array needs to be sorted.

		nums = [3,9,6]
Consider this example. We know that we can increment any number to turn it into any other number. That means, We can only take smaller elements and turn them into bigger elements. So for any random window in this array, we want a way to quickly get the biggest number so that we can then try turning all the elements into that number using the moves. And again, that's what sorting allows us to do. Because if we sort the array -

		nums = [3,6,9]
Now, no matter how big the window size is, the last element of the window will always be the biggest element so we can try to turn all the elements of that window to that last element by incrementing.

And now comes the interesting part. How to expand or shrink the window? What's the condition?

What we want is the window should have all the elements the same as the biggest element after doing at most K increments.

This also means that, the sum of the window after making all elements same as biggest should be =>

		(biggest element * number of elements in window)
			
		e.g. take the window [3,6] 
		If we turn all the elements into 6. Total sum will be 6 + 6  = 12 or (
		6 * number of elements in window)
But ofcourse it is not always possible to turn all elements of window into biggest element since we are restricted by the moves k.

Since we can use at most k moves, lets say we use all our moves to increment elements in a window. That basically means, whatever sum of the window was earlier, we added k to it.

	If we used all the k moves in a window
	New Sum = (sum before using k moves + k)
And now, for a valid window, we want to use at most k moves to convert all elements into biggest element. This means, we can combine the above two conditions together -

For a valid window - 

Total Sum of window after converting all elements to biggest element should be <= total sum of window after k increments

That is,


(biggest element * number of elements in window) <= (sum of window + k)
And that's the condition we have to use for checking for a valid window.

def maxFrequency(self, nums: List[int], k: int) -> int:
        maxFreq = 0
        
        # Sort the numbers first
        nums.sort()
        
        i,j = 0,0
        currSum = 0
        while j < len(nums):
            currSum += nums[j]
			# Since the array is sorted
            # The largest number for any window at any time is the current/jth element
            # So we want to know how many moves will it take to make all elements of this window = j
            # If each element becomes j, that means total sum will be nums[j] * number of elements in window
            # And we want that to be either less than or equal to sum of this window + moves we have
			# Because number of moves means how many we can add to a window so that each element is the same
            while nums[j] * (j - i + 1) > currSum + k: 
                currSum -= nums[i]
                i += 1
            
            # If we are here, that means, this is a valid window
            maxFreq = max(maxFreq, j - i + 1)
            j += 1
            
        return maxFreq
