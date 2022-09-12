
'''
Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.
'''


def __init__(self, nums: List[int]):
    self.nums = nums

def pick(self, target: int) -> int:
    cnt = idx = 0
    for i, num in enumerate(self.nums):
        if num != target:
            continue
        if cnt == 0:
            idx = i
            cnt = 1
        else:
            # this random will already give me numbers
            # between 0 and cnt inclusive
            # so for 2nd number I am getting random number 0 and 1
            # so each having a probability of 1/2
            # similarly for three numbers it will be 1/3
            rnd = random.randint(0, cnt)
            if (rnd == cnt):
                idx = i
            cnt += 1
    
    return idx
-----------------------------------------------------------------------------------------
from random import randint

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
		
	# Time complexity: O(n), where "n" is the length of self.nums
    def pick(self, target: int) -> int:
        # how many samples with value "target" we have seen so far
        n_samples = 0
		
		# result, selected index
        reservoir = 0
        
		# iterate over all the values in self.nums
        for index, value in enumerate(self.nums):
            if value == target:
				# target value is found, increment the number of samples with value "target" found so far
                n_samples += 1
				
				# if it is the first sample found, just keep it index
                if n_samples == 1:
                    reservoir = index
                else:
					# if there are more than 1 sample, randomly select any of them
                    nth_sample = randint(1, n_samples)
					
					# if the selected sample matches the first sample selected initially, then replace it
                    if nth_sample == 1:
                        reservoir = index
        return reservoir

----------------------------------------------------------------------------------------------------------
class Solution:

    def __init__(self, nums: List[int]):
        # Reservoir Sampling (which can handle the linked list with unknown size), time complexity O(n) (init: O(1), pick: O(n)), space complextiy O(1)
        self.nums = nums

    def pick(self, target: int) -> int:
        # https://docs.python.org/3/library/random.html
        count = 0
        chosen_index = None
        for i in range(len(self.nums)):
            if self.nums[i] != target:
                continue
            count += 1
            if count == 1:
                chosen_index = i
            elif random.random() < 1 / count:
                chosen_index = i
        return chosen_index

---------------------------------------------------------------------------------------
class Solution {

    private int[] nums;
    
    private Random rand;
    
    public Solution(int[] nums) {
        // Do not allocate extra space for the nums array
        this.nums = nums;
        this.rand = new Random();
    }
    
    public int pick(int target) {
        List<Integer> indices = new ArrayList<>();
        int n = this.nums.length;
        int count = 0;
        int idx = 0;
        for (int i = 0; i < n; ++i) {
            if (this.nums[i] == target) {
                indices.add(i);
            }
        }
        int l = indices.size();
        // pick an index at random
        int randomIndex = indices.get(rand.nextInt(l));
        return randomIndex;
    }
}
