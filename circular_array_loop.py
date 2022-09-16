'''
You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

If nums[i] is positive, move nums[i] steps forward, and
If nums[i] is negative, move nums[i] steps backward.
Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

A cycle in the array consists of a sequence of indices seq of length k where:

Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
Every nums[seq[j]] is either all positive or all negative.
k > 1
Return true if there is a cycle in nums, or false otherwise.
'''

def __init__(self):
        self.__visited = lambda x: not x # a cell i is visited when nums[i] = 0

def circularArrayLoop(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            if self.__visited(nums[i]):
                continue
            
            direction = nums[i] > 0
            
            # 1. Check if there is a cycle starting from i
            slow = fast = i
            while not (self.__visited(nums[slow]) or self.__visited(nums[fast])):
                
                slow = self.__next(nums, slow, direction)
                fast = self.__next(nums, self.__next(nums, fast, direction), direction)
                
                if slow == -1 or fast == -1:
                    break
                
                elif slow == fast:
                    return True
            
            # 2. Mark visited all cells that belong to the path starting from i
            slow = i
            while self.__next(nums, slow, direction) != -1:
                nums[slow], slow = 0, self.__next(nums, slow, direction)
            
        return False
        
    def __next(self, nums, idx, direction):
        if idx == -1: # To handle the case of next(next(fast)) = next(-1) = -1
            return -1
                
        elif (nums[idx] > 0) != direction: # check the direction
            return -1
        
        next_idx = (idx + nums[idx]) % len(nums)
        if next_idx < 0:
            next_idx += len(nums)
        
        return -1 if next_idx == idx else next_idx
      
-------------------------------------------------------------------------------------------

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n, visited = len(nums), set()
        for i in range(n):
            if i not in visited:
                local_s = set()
                while True:
                    if i in local_s: return True
                    if i in visited: break          # credit to @crazyhyz, add this condition to avoid revisited
                    visited.add(i)
                    local_s.add(i)
                    prev, i = i, (i + nums[i]) % n
                    if prev == i or (nums[i] > 0) != (nums[prev] > 0): break
        return False
