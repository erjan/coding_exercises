def f2(nums,k):

    for i in range(len(nums)-k+2):
        for j in range(i, i+k):
            for t in range(i,j):
                print(nums[t], end = ' ')
            print()
        print()

a = [1,2,6,7,10,12,16,5,45,34,8,0,56,3,23,23,0,7]
f2(a,5)
print('length of array %d' % len(a))

print(a)
print(a[-4:])
print(a[17])
print(a[16])


