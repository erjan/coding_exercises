'''
You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e., 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e., perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

Given an integer n, the length of the array, return the minimum number of operations needed to make all the elements of arr equal.
'''

class Solution:
    def minOperations(self, n: int) -> int:
        
        s = n*(n+1)//2
        
        t = s//n
        moves = 0
        
        a = [i for i in range(1,n+1)]
        
        for i in range(len(a)):
            
            if a[i] != t:
                moves += abs(a[i] -t)
        return moves
      
--------------------------------------------------------------------------------------------------------------------------



'''
Idea:
This problem has a very simple mathematical solution.

The obvious thing here is that the array formed by the instructions is a linear progression. Mathematically, it should also be obvious that the value to which we need to make each element of our array is the same value found at the middle of the array.

If we were to follow the literal instructions, we could move outward from the middle point and repeatedly shift 1 from the right (higher) side to the left (lower) side. This process would lead to a triangular number of operations, modified by the fact that each value starts off 2 less/more than the ones on either side, rather than 1.

Take, for example, the case of n = 7, or [1,3,5,7,9,11,13]. We would perform the operation twice on the 5 & 9 pair, four times on the 3 & 11 pair, and six times on the 1 & 13 pair, bringing all values to the median of 7 with a total of 12 operations.

The sum of linearly increasing numbers is the very definition of a triangular number, which is in this case doubled because the numbers are 2 apart, rather than 1. The standard formula for a triangular number is n * (n + 1) / 2. Since our triangular number is only half the length of array, not counting the middle, that equates to 2 * ((n - 1) / 2) * ((n - 1) / 2 + 1) / 2, which simplifies to (n^2 - 1) / 4.

But that's when n is odd and the middle is conveniently a point. What if n is even?

If n is even, then it becomes a slightly different formula, with the midpoint being halfway between the two middle points (which is incidentally why the problem specified a 2 value difference in each array element, to prevent impossible fractions). In this case, we're doing the same process, only on (n - 2) / 2 elements rather than (n - 1) / 2 elements, omitting the two "middle" elements.

This will leave the entire left side of the array equal to the left-middle element, and the entire right side of the array equal to the right-middle element. In order to even the entire array, we'll just need another n / 2 operations to move the right side down 1 and the left side up 1.

That formula becomes 2 * ((n - 2) / 2) * ((n - 2) / 2 + 1) / 2 + n / 2, which simplifies nicely down to n^2 / 4.

Thus the only difference between the two formulas is the - 1 present in the odd version, which is basically the rounding error if n is odd, and can be corrected by flooring (or double bitwise NOT'ing) the result.

On a more intuitive note, if you think of the array as points forming a line on a graph, then you can think of that line as the diagonal of a box of area n * 2n, or 2n^2. If you then think of the triangle of moves that have to be made, you can note that the area of said triangle is 1/8th the area of the box, or 2n^2 / 8, or n^2 / 4
'''

class Solution:
    def minOperations(self, n: int) -> int:
        return n * n // 4   
      
--------------------------------------------------------------------------------------
class Solution:
    def minOperations(self, n: int) -> int:
        if(n%2!=0):
            n=n//2
            return n*(n+1)
        else:
            n=n//2
            return n**2
