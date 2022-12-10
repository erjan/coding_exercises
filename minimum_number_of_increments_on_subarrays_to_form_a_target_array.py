'''
You are given an integer array target. You have an integer array initial of the same size as target with all elements initially zeros.

In one operation you can choose any subarray from initial and increment each value by one.

Return the minimum number of operations to form a target array from initial.

The test cases are generated so that the answer fits in a 32-bit integer.
'''

Why does this work?

First, we need to add the first element of the array. There are no prior elements to leech off of.

Then consider any successive element. We can "reuse" up to the value 
of the previous element by simply extending the subarray we're adding to by one. Anything more than that, we need to increment.


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        return sum(max(target[i - 1] - target[i], 0) for i in range(1, len(target))) + target[-1]
