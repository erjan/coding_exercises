#Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

#bruteforce solution - TLE
def f(nums):
    n = nums
    max_len = 0
    for i in range(len(n)):
        for j in range(i,len(n)):
            k = i
            temp = []
            while(k <= j):
                temp.append(n[k])

                k+=1

            if temp.count(0) == temp.count(1):
                if len(temp) > max_len:
                    max_len = len(temp)
    print(max_len)
    return max_len
            

 
n = [0,0,0,0,0,1,1,1,0,0,1,0,0,0]
f(n)
