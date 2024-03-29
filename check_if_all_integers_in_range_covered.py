'''
You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.
'''

#my own solution

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right+1):

            for r in range(len(ranges)):
                interval = ranges[r]
                print('----------------')
                print('interval: ', interval, ' and the i: ', i)

                start = interval[0]
                end = interval[1]
                temp = list()
                if i >= start and i <= end:
                    temp.append(True)
                    print('ok good')
                    break
                else:
                    temp.append(False)

                print('temp')
                print(temp)
            if all(temp) == False:
                print('baaaad')
                return False

            
#a bit optimized solution:
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right+1):

            for l, r in ranges:             
                temp = list()
                if i >= l and i <= r:
                    temp.append(True)
                    break
                else:
                    temp.append(False)
            if all(temp) == False:
                return False
        return True

#really good elegant solution

 def isCovered(self, ranges, left, right):
        return all(any(l <= i <= r for l, r in ranges) for i in xrange(left, right + 1))
