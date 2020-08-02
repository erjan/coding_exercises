'''
Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 

Return how many groups have the largest size.
'''


class Solution:
    def countLargestGroup(self, n: int) -> int:
        list_sums = dict.fromkeys([i for i in range(1,37)])
        for i in list_sums.keys():
            list_sums[i] = 0

        for i in range(1,n+1):
            num = str(i)
            num = list(num)
            num = list(map(lambda s: int(s),num))
            temp_sum = sum(num)
            if temp_sum in list_sums.keys():
                list_sums[temp_sum]+=1

        max_size = max(list_sums.values())
        result= 0
        for k in list_sums.keys():
            if list_sums[k] == max_size:
                result+=1
        print(result)
        return result

    
#a bit simplified solution

def f(n):
    list_sums = dict.fromkeys([i for i in range(1,37)])
    for i in list_sums.keys():
        list_sums[i] = 0

    for i in range(1,n+1):
        num = str(i)
        num = [int(c) for c in num]
        if sum(num) in list_sums.keys():
            list_sums[sum(num)]+=1

    max_size = max(list_sums.values())
    result= 0
    for k in list_sums.keys():
        if list_sums[k] == max_size:
            result+=1
    return result

f(2)
