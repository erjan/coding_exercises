'''
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.
'''

class Solution:
    def minJumps(self, arr):
        n, dict1 = len(arr), defaultdict(list)

        for i,j in enumerate(arr):
            dict1[j].append(i)

        stack, visited, visited_group = [(0,0)], set(), set()

        visited.add(0)

        while stack:
            idx, jump = stack.pop(0)

            if idx == n-1:
                return jump

            if idx+1 < n and idx+1 not in visited:
                visited.add(idx+1)
                stack.append((idx+1,jump+1))

            if idx-1 >= 0 and idx-1 not in visited:
                visited.add(idx-1)
                stack.append((idx-1,jump+1))

            if arr[idx] not in visited_group:
                for j in dict1[arr[idx]]:
                    if j not in visited:
                        visited.add(j)
                        stack.append((j,jump+1))
                visited_group.add(arr[idx])

                

---------------------------------------------------------------------------------------------
class Solution:
    def minJumps(self, arr):
        n, dict1 = len(arr), defaultdict(list)

        for i,j in enumerate(arr):
            dict1[j].append(i)

        stack, visited, visited_group = [(0,0)], set(), set()

        visited.add(0)

        while stack:
            idx, jump = stack.pop(0)

            if idx == n-1:
                return jump

            if idx+1 < n and idx+1 not in visited:
                visited.add(idx+1)
                stack.append((idx+1,jump+1))

            if idx-1 >= 0 and idx-1 not in visited:
                visited.add(idx-1)
                stack.append((idx-1,jump+1))

            if arr[idx] not in visited_group:
                for j in dict1[arr[idx]]:
                    if j not in visited:
                        visited.add(j)
                        stack.append((j,jump+1))
                visited_group.add(arr[idx])

                

