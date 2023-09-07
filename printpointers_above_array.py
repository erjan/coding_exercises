def printpointers_above_array(nums, left, right):
    print()
    for i in range(len(nums)):
        if i == left or i == right:
            print("V", end=" ")
        else:
            print(" ", end=" ")
    print()
    for i in range(len(nums)):
        print(nums[i], end=" ")
    print()
