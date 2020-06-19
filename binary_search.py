import random

def binary_search(val, arr):
    low = 0
    high = len(arr)
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

l = random.sample( range(14000),390)

l = sorted(l)

binary_search(l[125],l)
