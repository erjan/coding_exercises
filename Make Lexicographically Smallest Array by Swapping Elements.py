You are given a 0-indexed array of positive integers nums and a positive integer limit.

In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.

Return the lexicographically smallest array that can be obtained by performing the operation any number of times.

An array a is lexicographically smaller than an array b if in the first 
position where a and b differ, array a has an element that is less than 
the corresponding element in b. For example, the array [2,10,3] is 
lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10.

-------------------------------------------

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        # Pair each number with its index and sort by the number
        sorted_enum = sorted((num, i) for i, num in enumerate(nums))
        
        new_positions = []
        curr_positions = []
        prev = float('-inf')
        
        for num, idx in sorted_enum:
            # If the current number exceeds the previous number by more than the limit,
            # sort and append the current positions to the result
            if num > prev + limit:
                new_positions.extend(sorted(curr_positions))
                curr_positions = [idx]
            else:
                curr_positions.append(idx)
            prev = num
        
        # Append any remaining positions
        new_positions.extend(sorted(curr_positions))
        
        # Construct the result array using the new positions
        res = [0] * n
        for i, idx in enumerate(new_positions):
            res[idx] = sorted_enum[i][0]
        
        return res
