'''
You are given an integer array arr. Sort the integers in the array in ascending 
order by the number of 1's in their binary representation and in case of 
two or more integers have the same number of 1's you have to sort them in ascending order.
Return the array after sorting it.
'''
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = dict()
        nums= arr
        for i in nums:
            count = bin(i).count('1')
            if count not in d:
                d[count] = [i]
            else:
                d[count].append(i)
        res = list()

        for i in sorted(d.keys()):
            res.extend(sorted(d[i]))

        print(res)
        return res
