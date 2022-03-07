'''
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
'''

def summaryRanges(nums):
    if not nums:
        return nums
    output, temp = [], [nums[0]]

    for i in range(1, len(nums)):
        print('temp------')
        print(temp)
        print()
        if nums[i] - temp[-1] == 1:
            temp.append(nums[i])
        else:
            res = str(temp[0]) + '->' + str(temp[-1]) if len(temp) > 1 else str(temp[0])
            output.append(res)
            temp = [nums[i]]
    res = str(temp[0]) + '->' + str(temp[-1]) if len(temp) > 1 else str(temp[0])
    output.append(res)

    return output
