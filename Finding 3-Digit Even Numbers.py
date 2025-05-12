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
        res = set()
        n = len(digits)
        freq = dict(Counter(digits))
        for i in range(100,1000,2):
            
            cur = list(map(int, str(i)))

            fr2 = dict(Counter(cur))
            st = True
            for k,v in fr2.items():
                
                if k not in freq or freq[k] < v:
                    st = False
                    break
            if st:
                res.add(i)
        
        res = sorted(list(res))
        return res
