'''
Given an m x n matrix mat where every row is sorted in strictly increasing order, return the smallest common element in all rows.

If there is no common element, return -1.

 

Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
Example 2:

Input: mat = [[1,2,3],[2,3,4],[2,3,5]]
Output: 2
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 104
mat[i] is sorted in strictly increasing order.
'''



class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # We know 1 element in the first row must be in the others.
        for i in mat[0]:
		    # Keep track every time we find the cur i val in another row.
            finds = 0
			# Scan through the other rows.
            for row in mat[1:]:
			    # If we find the element += 1 finds.
                if row[bisect.bisect_left(row, i)] == i:
                    finds += 1
                    continue
                else:
                    break
			# If we have a find in every row return the val i.
            if finds + 1 == len(mat):
                return i
		# Otherwise we know there wasn't a common val in all rows.
        return -1
----------------------------------------------------

O( R log C ):

This program works by iterating through every element in the first row of the matrix, checking to see whether it is in all the other rows. This is done by taking the first number in the first row and then doing a binary search for that number in each of the successive rows. This is acceptable since each of the rows are already sorted. If the number is not found in a given row, the inner for loop immediately breaks and we go on to the next number in the first row. If a number in the first row is found to be in every other row, the program returns that number. If the outer for loop iterates through every number in the first row and cannot find a single number that is in all the other rows, the for loop completes and the next command returns -1. The binary search of each row is done by using the bisect function which finds the index of where that element would be inserted. If the value in the row of the matrix at that index is the number from the first row, then a match was successfully found in that row. Otherwise the number does not exist in that row. Each binary search of a row of C elements takes O (log C) time. Since there are R rows to search, the overall time is O (R log C).

class Solution:
    def smallestCommonElement(self, A: List[List[int]]) -> int:
    	M = len(A)
    	for i in A[0]:
    		for j in range(1,M):
    			I = bisect.bisect_left(A[j],i)
    			if A[j][I] != i: break
    		if A[j][I] == i: return i
    	return -1
		
		
O( R·C ):

The program starts by creating a list R which consists of all the elements in the matrix (from the second row to the last row) in a flattened 1D form. Note that the numbers in the first row are not included in list R. The program then loops through each element in the first row and counts how many times it occurs in list R. If an element occurred in every row in the original matrix A then it should occur M - 1 times in list R, where M is the number of rows in matrix A. If the count comes out to M - 1, the number in the first row is returned. If not, the next number in the first row is tested. If none of the numbers in the first row have a count of M - 1, the for loop ends and -1 is returned. Since each count of a row requires C tests and we are also looping through each of the C numbers in the first row and there are R rows in total, the time for this approach is O( R·C ).

class Solution:
    def smallestCommonElement(self, A: List[List[int]]) -> int:
    	M, R = len(A), sum(A[1:],[])
    	for i in A[0]:
    		if R.count(i) == M - 1: return i
    	return -1
----------------------------------------------------------------------

The core idea here it's the smallest common element in all rows.
Hence the element should definitely be one of the elements in the first row itself.
We iterate through the elements in the first row (which is in sorted order) - so the moment we find that element is there in all the other rows we can instantly return it.
We have to search, if the element under consideration is there in all the other rows, which are also sorted.
So we just apply binary search on the rest of the rows, for the element of interest (the elements in the first row)
from bisect import bisect_left, bisect_right

class Solution:
    def binary_search(self, array, val):
        index = bisect_left(array, val)
        if index != len(array) and array[index] == val:
            return index
        else:
            return -1
    
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        values = mat[0]
        mat.pop(0)
        
        for i, val in enumerate(values):
            flag = True
            for arr in mat:
                idx = self.binary_search(arr, val)
                if idx == -1:
                    flag = False
                    break
            if flag:
                return val
            
        return -1
--------------------------------------------------------------------------------------------------------

The key issue here is how to use the fact the rows are sorted. The trick is if there is very few elements in ans, we can binary search every elements in ans in the next row (O(log(n))), instead of going through all the elements in the next row (O(n)). The extreme case is where ans only has one element, then we can just binary search that element only. The threshold is math.log2(len(row)).

Another trick is early exit. If ans becomes empty, return immediately.

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        power = int(math.log2(len(mat[0])))
        ans = set(mat[0])
        for r in mat[1:]:
            if len(ans) > power:
                ans &= set(r)
            else:
                ans = set(a for a in ans if r[bisect.bisect_left(r, a)] == a)
            if not ans:
                break
        return sorted(ans)[0] if ans else -1
---------------------------------------------------------

Idea: create a dictionary with counts of all elements. What we need is a key, which has a value equal to len(mat).
Because list comprehensions don't fully support if/else statements (in a way we need for this problem), we will first take care of the case when there is no common element and after that will proceed to returning a required element.

def smallestCommonElement(mat):
    d = {}
    for el in mat:
        for i in el:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
    if len(mat) not in d.values():
        return -1
    else:
        return [k for k,v in d.items() if v == len(mat)][0]
--------------------------------------------------------------------------------

from functools import reduce

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # N - number of rows, M - number of columns
        # Convert each row into a set in O(NM)
        sets = [set(r) for r in mat]
        # Reduce rows to a single set in O(NS),
        # where S is the size of a set converted
        # from a row of size M on the previous step
        union = reduce(lambda x, y: x & y, sets)
        # Find the minimum element in O(U), where U is the size of the reduced set,
        # or return -1, if the set is empty
        ans = min(union) if union else -1
        # Total time and space complexity is O(NM)
        return ans
Convert the above code into two lines

from functools import reduce

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        union = reduce(lambda x, y: x & y, [set(r) for r in mat])
        return min(union) if union else -1
------------------------------------------------------      
      
      
      
    
    
