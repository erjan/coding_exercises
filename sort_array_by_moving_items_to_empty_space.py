'''
You are given an integer array nums of size n containing each element from 0 to n - 1 (inclusive). Each of the elements from 1 to n - 1 represents an item, and the element 0 represents an empty space.

In one operation, you can move any item to the empty space. nums is considered to be sorted if the numbers of all the items are in ascending order and the empty space is either at the beginning or at the end of the array.

For example, if n = 4, nums is sorted if:

nums = [0,1,2,3] or
nums = [1,2,3,0]
...and considered to be unsorted otherwise.

Return the minimum number of operations needed to sort nums.

'''



'''
In the end, zero can only be in the front or in the back.
Let's only look at case that final zero is in the front. In this case, final nums should look like this [0,1,2,3,...], all number should equal to its index. Final positon of number "1" should be at index "1", final positon of number "2" should be at index "2", ...
If zero is at index 3, then we swap zero with the number "3". After swap, the number "3" goes to index "3", which is its final position, and "zero" goes to a new position that could be anywhere. We then go to the new "zero" again, and swap it with the number equal to the index of zero. Keep doing so until finish.

We can keep doing so as long as zero doesn't go to index "0". If after swap, "zero" happen to be on index "0", then we cannot continue swapping zero anymore. In this case, we should scan the whole nums, find the first number that isn't in its final position, swap it with zero. After such swap, zero is not at index "0", and we can continue swapping zero the above way.

After finish, we do the same thing all over again for the case that zero's final position is in the back, not in the front, like nums==[1,2,3,..., 0]. We do the same thing, just that this time all numbers should equal to its index+1. Final position of number "1" should be at index "2", final position of number "2" should be at index "3", ...

Time complexity: O(n)
'''

class Solution:
    def sortArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        # target: [0, 1, 2, ..., n-1]
        loc = {x: i for i, x in enumerate(nums) if i != x or x == 0}
        c1 = 0
        cur = loc.pop(0)
        while cur != 0 or loc:
            # if empty space not at begin, then swap with the number should be at this space (which is the index)
            if cur != 0:
                new_cur = loc[cur]
                del loc[cur] # delete since already in the right position
                cur = new_cur
            # else pick one from candidates where index != num
            else:
                k, v = loc.popitem()
                cur, loc[k] = v, cur # swap position since still need to reassign in the future
            c1 += 1
            
        if c1 == 0: return c1

        # target: [1, 2, ..., n-1, 0]
        loc = {x: i for i, x in enumerate(nums) if i + 1 != x or x == 0}
        c2 = 0
        cur = loc.pop(0)
        while cur != n - 1 or loc:
            if cur != n - 1:
                new_cur = loc[cur + 1]
                del loc[cur + 1]
                cur = new_cur
            else:
                k, v = loc.popitem()
                cur, loc[k] = v, cur
            c2 += 1
        
        return min(c1, c2)
      
-----------------------------------------------------------------------------------------------------------
    def sortArray(self, nums: List[int]) -> int:
        def process(nums,final_zero_idx):
            res = 0
            idxs = {v:i for i,v in enumerate(nums)}
            process_idx = 1 if final_zero_idx==0 else 0
            def swap_zero_to(i):
                nonlocal res
                num = nums[i]
                zero_idx = idxs[0]
                nums[zero_idx],nums[i]=nums[i],nums[zero_idx]
                idxs[num],idxs[0]=zero_idx,i
                res+=1
            offset = 0 if final_zero_idx==0 else 1
            while True:
                num = idxs[0]+offset # the number to swap with zero
                if idxs[0] != final_zero_idx: 
                    swap_zero_to(idxs[num])
                else: # cannot swap zero if zero is at final_zero_idx
                    # swap the first number that isn't on its final position
                    while process_idx<len(nums) and nums[process_idx]==process_idx+offset:
                        process_idx+=1
                    if process_idx==len(nums)-offset:
                        return res
                    swap_zero_to(idxs[nums[process_idx]])
            return res
        return min(process(nums[:],0),process(nums[:],len(nums)-1))








