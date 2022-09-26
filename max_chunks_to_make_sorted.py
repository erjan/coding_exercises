'''
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.
'''

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:

        # Intialize the stack
        stack = []

        # Iterate through all numbers
        for num in arr:

            # Initialize the range of the current partition
            minVal, maxVal = num, num

            # While the current partition isn't greater than a previous partition on top of the stack, mergethem together
            while stack and stack[-1][1] > minVal:
                minVal, maxVal = min(minVal, stack[-1][0]), max(maxVal, stack[-1][1])
                stack.pop()

            # Add the current parition onto the stack
            stack.append((minVal, maxVal))

        return len(stack)
