'''
You are given an integer finalSum. Split it into a sum of a maximum number of unique positive even integers.

For example, given finalSum = 12, the following splits are valid (unique positive even integers summing up to finalSum): (12), (2 + 10), (2 + 4 + 6), and (4 + 8). Among them, (2 + 4 + 6) contains the maximum number of integers. Note that finalSum cannot be split into (2 + 2 + 4 + 4) as all the numbers should be unique.
Return a list of integers that represent a valid split containing a maximum number of integers. If no valid split exists for finalSum, return an empty list. You may return the integers in any order.

 
 '''


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        arr = []
        if finalSum % 2 == 0: # If finalSum is odd then we cannot ever divide it with the given conditions
            a, i = finalSum // 2, 1 # a is the number of 2's and i is the number of 2's that we will use to form a even number in the current iteration
            while i <= a: # Till we have sufficient number of 2's available
                arr.append(2*i) # Join the i number of 2's to form a even number
                a -= i # Number of 2's remaining reduces by i
                i += 1 # Number of 2's required in next itertation increases by 1
            s = sum(arr)
            arr[-1] += finalSum - s # This is done if their were still some 2's remaining that could not form a number due to insufficient count, then we add the remaining 2's into the last number.
        return arr
