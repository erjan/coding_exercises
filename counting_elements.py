def f(arr):
    s = set(arr)
    count = 0
    for i in range(len(arr)):
        check = arr[i]+1
        if check in s:
            count+=1
    print(count)
    return count


arr = [1,1,3,3,5,5,7,7]

arr = [1,3,2,3,5,0]


f(arr)

