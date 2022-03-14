'''
You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:

The integer consists of the concatenation of three elements from digits in any arbitrary order.
The integer does not have leading zeros.
The integer is even.
For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.
'''

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        nums = digits
        s = ''
        for n in nums:
            s += str(n)
        print(s)
        res = list(set(itertools.permutations(s, 3)))

        for i in range(len(res)):
            res[i] = int(''.join(res[i]))

        res = list(filter(lambda x: x % 2 == 0, res))
        res = list(filter(lambda x: len(str(x)) == 3, res))
        res.sort()
        print(res)
        return res
