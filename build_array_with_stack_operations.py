'''
You are given an array target and an integer n.

In each iteration, you will read a number from list = [1, 2, 3, ..., n].

Build the target array using the following operations:

"Push": Reads a new element from the beginning list, and pushes it in the array.
"Pop": Deletes the last element of the array.
If the target array is already built, stop reading more elements.
Return a list of the operations needed to build target. The test cases are generated so that the answer is unique.
'''


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        arr = list()
        cur = 0
        for i in range(1, n+1):
            print('--------------------')
            print(i)
            if cur >= len(target):
                print('breaking out')
                break
            elif i == target[cur]:
                print('match')
                arr.append('Push')
                cur += 1

            else:
                arr.append('Push')
                arr.append('Pop')

        print(arr)
        return arr
