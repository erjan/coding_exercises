'''
You are given a 0-indexed array nums consisting of positive integers, representing targets on a number line. You are also given an integer space.

You have a machine which can destroy targets. Seeding the machine with some nums[i] allows it to destroy all targets with values that can be represented as nums[i] + c * space, where c is any non-negative integer. You want to destroy the maximum number of targets in nums.

Return the minimum value of nums[i] you can seed the machine with to destroy the maximum number of targets.
'''

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        mapping = defaultdict(list)
        for num in nums:
            mapping[num % space].append(num)
        
        # print(mapping) # defaultdict(<class 'list'>, {1: [3, 7, 1, 1, 5], 0: [8]}) groups is [3, 7, 1, 1, 5] and [8] 
        """ min of [3, 7, 1, 1, 5] can destroy all others (greedy approach) => 1 can destory 1,3,5,7 ... """
        performance = defaultdict(list)
        for group in mapping.values():
            performance[len(group)].append(min(group))
        
        # print(performance) # defaultdict(<class 'list'>, {5: [1], 1: [8]})
		""" nums that can destory 5 targets are [1], nums that can destory 1 target is [8] """
        return min(performance[max(performance)])
    
