'''
Alice manages a company and has rented some floors of a building as office space. Alice has decided some of these floors should be special floors, used for relaxation only.

You are given two integers bottom and top, which denote that Alice has rented all the floors from bottom to top (inclusive). You are also given the integer array special, where special[i] denotes a special floor that Alice has designated for relaxation.

Return the maximum number of consecutive floors without a special floor.



Explanation
Sort special floors.
The max consecutive floors between special is A[i] - A[i-1] - 1
The top consecutive floors is top - A[n - 1]
The bottom consecutive floors is A[0] - bottom



The idea here is to get the difference between all the special floors, including the bottom and top.

Arrange the special array in sorted order.
Now bottom should be added at the start, as we want to get the difference of floors from bottom to first element of the sorted special array.
But notice a Pattern, we donot include the special relaxation floors. But we need to include the bottom and top floors if they are not special floors.
So, following a general idea that nothing in the array will be included in the difference we are calculating. So, the bottom is added as bottom - 1, meaning do not include bottom - 1 but include bottom.
Similarly top should be added, but both top and top -1 should be considered if they are not in the special array. So add top + 1 inplace of just top.
Then, simply calulate the max difference.

That's it.

The full code (written during contest) is given below:
'''


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        special.insert(0, bottom - 1)
        special.append(top + 1)
        
        ans = 0
        for i in range(len(special)-1):
            ans = max(ans, special[i+1] - special[i] - 1)
        return ans



