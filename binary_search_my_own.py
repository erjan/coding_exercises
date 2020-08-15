import random

def binary_search(val, arr):
    if arr == None or len(arr) == 0:
        return -1
    low = 0
    high = len(arr)-1
    mid = 0
    print('looking for value %d' % val)
    while low <=high:
        print('-------------------------array------------------------------')
        print('from index %d to %d' %(low,high))
        print(arr[low:high])
        mid = (low + high)//2
        if arr[mid] == val:
            print('found VALUE! at index %d' % mid)
            return mid
        elif arr[mid] > val:
            high = mid-1
        elif arr[mid] < val:
            low = mid+1
    print('no value found! -1')
    return -1

l = random.sample( range(14000),390)
l = [1,2,5,7,11,15,20]
l = sorted(l)

#test cases:
binary_search(-10, l)
binary_search(0, l)
binary_search(1, [])
binary_search(1, None)
binary_search(0, [1,2,3])
binary_search(10,[1,2,3,20,30,40,50])
binary_search(30, l)

