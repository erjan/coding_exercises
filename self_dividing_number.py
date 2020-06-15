'''
Given a lower and upper number bound, 
output a list of every possible self dividing number, including the bounds if possible.
'''

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        temp = list()
        for i in range(left, right+1):
            as_str = str(i)
            #print(as_str)
            if as_str.count('0') != 0:
                continue
            else:
                temp.append(i)
        res = list()

        for num in temp:
            as_str = str(num)
            status = True
            for ch in as_str:

                if num % int(ch) != 0:
                    status = False
            if status:
                    res.append(num)

        return res
