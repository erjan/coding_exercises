'''
An element x of an integer array arr of length m is dominant if more than half the elements of arr have a value of x.

You are given a 0-indexed integer array nums of length n with one dominant element.

You can split nums at an index i into two arrays nums[0, ..., i] and nums[i + 1, ..., n - 1], but the split is only valid if:

0 <= i < n - 1
nums[0, ..., i], and nums[i + 1, ..., n - 1] have the same dominant element.
Here, nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j, both ends being inclusive. Particularly, if j < i then nums[i, ..., j] denotes an empty subarray.

Return the minimum index of a valid split. If no valid split exists, return -1.
'''

#ugly not working solution - 155/900 cases pass!
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        


        freq =  dict(Counter(nums))
        freq = sorted(freq.items(), key = lambda x: x[1],reverse=True)
        fr = freq[0][1]
        dominant = freq[0][0]
        
        res = -1
        print(f'overall frequency is: {fr}')
        n = len(nums)

        for i in range(n-2):

            sub1 = nums[:i]
            sub2 = nums[i:]

            if i >0:

                freq1 = dict(Counter(sub1))
                freq1 = sorted(freq1.items(), key = lambda x: x[1],reverse=True)
                freq1_dominant_element = freq1[0][0]
                freq1_dominant_value = freq1[0][1]
            
                freq2_dominant_value = fr-freq1_dominant_value

                if freq1_dominant_element == dominant:
                    res = i
                    print(f'its {i}')
                    break
        return -1

----------------------------------------------------
def minimumIndex(nums):
    from collections import Counter

    freq = Counter(nums)
    n = len(nums)
    dom, count = 0, 0

    for num, c in freq.items():
        if c > n // 2:
            dom, count = num, c
            break

    left_count = 0
    for i in range(n - 1):
        if nums[i] == dom:
            left_count += 1
        left_size = i + 1
        right_size = n - left_size
        right_count = count - left_count

        if left_count > left_size // 2 and right_count > right_size // 2:
            return i

    return -1


