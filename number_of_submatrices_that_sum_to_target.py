'''
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.
'''

class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        dp, ans = {}, 0
        for k in range(m):
            t = [0] + list(accumulate(matrix[k]))
            for i, j in combinations(range(n+1), 2):
                dp[i, j, k] = dp.get((i,j,k-1), 0) + t[j] - t[i]
        
        for i, j in combinations(range(n+1), 2):
            T = Counter([0])
            for k in range(m):
                ans += T[dp[i, j, k] - target]
                T[dp[i, j, k]] += 1
                
        return ans
      
---------------------------------------------------------------------------------------------
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # get your rows and cols of the matrix 
        rows = len(matrix)
        cols = len(matrix[0])
        # check for transpose needs 
        if rows > (cols*cols) : 
            temp = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
            matrix = temp 
            rows = len(matrix)
            cols = len(matrix[0])
        # matrix prefix sums of size rows + 1 x cols + 1 
        # outside row and cols will be zero. This allows for augment to consider those cases that would fall outside our array set up 
        matrix_prefix_sums = [[0 for _ in range(cols + 1)] for _ in range(rows+1)]
        # loop your matrix to get your prefix sums 
        for row in range(1, rows+1) : 
            for col in range(1, cols+1) : 
                # each prefix sum is the sum of value up, value back, and value current (using 1 offset) and value up and back 
                value_up = matrix_prefix_sums[row-1][col]
                value_back = matrix_prefix_sums[row][col-1]
                value_up_and_back = matrix_prefix_sums[row-1][col-1]
                matrix_prefix_sums[row][col] = matrix[row-1][col-1] + value_up + value_back - value_up_and_back
        # end for loop 
        # final answer format 
        number_of_sub_arrays = 0 
        # need to loop again, this time considering our sub array of prefixes as a sub array sum instance problem 
        # for the sub array sum equal to target, this is a combination of a cumulative sum with a hashmap 
        # the hashmap tracks the number of sub arrays up to this point that have been of value target 
        # we let our hashmap row index 1 loop all of our rows for our prefix sums considerations 
        # incidentally, for a standard one line array, we can use much of lines 29-51
        # we'd just really need to implement our sum outside the col loop as zero and start with our answers above the col loop 
        # then you could just add the sum as you go along instead of switching to a new prefix sum 
        for row_index_1 in range(1, rows+1) : 
            # our second hashmap row index 2 will loop from row index 1 to rows + 1 due to that augment at the top 
            for row_index_2 in range(row_index_1, rows+1) : 
                # at each instance of our sub array of prefix sums, we need a hashmap 
                # dictionary originally only containing 0 and 1 
                prefix_subarray_sums = {0:1}
                # now we can loop over the column indices in our prefix sums 
                for col_index in range(1, cols+1) : 
                    # get our stored prefix sum with offset for the row index 1 valuation. This is why we want bounding 0 lines
                    # if we end up at a spot where the row back is out of bounds, that's a zero value 
                    # but that's okay, as that's what we used already! 
                    prefix_sum = matrix_prefix_sums[row_index_2][col_index] - matrix_prefix_sums[row_index_1 - 1][col_index]
                    # check if we have already found this valuation 
                    # we can do this with a hash key equal to our prefix_sum - target 
                    hash_key = prefix_sum - target 
                    # if we have found the value of prefix_sum - target in our prefix_subarray_sums, we can increment our answer by that
                    if hash_key in prefix_subarray_sums : 
                        number_of_sub_arrays += prefix_subarray_sums[hash_key]
                    # if we have never had this prefix sum, add it as a new key 
                    if prefix_sum not in prefix_subarray_sums : 
                        prefix_subarray_sums[prefix_sum] = 0
                    # increment our prefix sub array sum by 1 at this prefix sum as it has been reached now 
                    # each new time it is reached, we are noting the number of times this sum occurred on our path over the columns 
                    # now, if we end up having prefix_sum - target in their, we either have a value that is 0 
                    # or we have a value that is prefix sum a - target = prefix sum b 
                    # this means we have a sub array combination that would work, and why we update on line 41 for our answer 
                    prefix_subarray_sums[prefix_sum] += 1 
                # end col for loop 
            # end row 2 for loop 
        # end row 1 for loop 
        # return the number of sub arrays found 
        return number_of_sub_arrays
