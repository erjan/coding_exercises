'''
Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.
'''

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
		# special cases: k == 1,  k == m * n
        if k == 1: 
            return 1
        if k == m * n: 
            return m * n
		# make the matrix a tall one - height >= width 
		# because later I will loop along the width. This will reduce the time
        if n >= m: 
            m, n = n, m
        
		# set the left, right boundaries and the ranks (the largest ranks for the values)
		# e.g. in a 3 * 3 table, number 2 shows up twice, taking up ranks from 2 to 3
		# so the largest rank here is 3 for number 2. 
        left = 1
        # left_rank = 1
        right = m * n
        # right_rank = m * n
        
		# binary search loop
        while right - left > 1: 
            mid = (left + right) // 2
			# mid_rank is the largest rank of the number
            mid_rank = 0
			
			# find the number of columns whose maximum < mid
			# (mid - 1) is to prevent counting the column with maximum == mid.
            num_cols = (mid - 1) // m
            residual = mid - num_cols * m
            mid_rank += num_cols * m
            
			# flag to track if mid is a valid value in the table
            flag = 0
            for i in range(num_cols + 1, n + 1): 
                if i == mid: 
                    mid_rank += 1
                    break
                else: 
                    mid_rank += mid // i
                    if mid % i == 0: 
                        flag = 1
            if flag == 1: 
				# mid is a valid number in the table
				# if mid_rank == k: mid's largest rank is k and mid is the kth number
				# if mid_rank < k: kth number > mid, so left = mid
				# if mid_rank > k: mid's largest rank > k but mid still can be the kth number but kth number can be no larger than mid, so right = mid
                if mid_rank == k: 
                    return mid
                elif mid_rank > k: 
                    right = mid
                else: 
                    left = mid
            else: 
				# mid is not a valid number in the table
				# if mid_rank == k, it means there are k values in the table smaller than mid
				# so there is a number smaller than mid ranking the kth. 
				# mid_rank > k or mid_rank < k:  similar operation as above
                if mid_rank >= k: 
                    right = mid
                else: 
                    left = mid
        
		# In case the while loop breaks out without returning
		# let's assume when right - left == 2 and mid == left + 1. The solution must be among the three. 
		# right with its largest rank > k
		# left with its largest rank < k
		# Scenario 1. if mid is a valid number in the table
		## 1a. if mid_rank < k: right has its rank from mid_rank + 1 (<= k) till right_rank (> k)
		## 1b. if mid_rank > k: right = mid. Now right (== mid) has its rank from left_rank + 1 (<= k) till mid_rank (> k)
		## in both cases, right is the solution
		# Scenario 2. if mid is not a valid number in the table then we can just ignore mid and imply the solution is right. 
		## But step by step, as mid is not in the table, mid_rank == left_rank, so left = mid. 
		## So right has its rank from mid_rank + 1 (i.e. left_rank + 1) (<= k) till right_rank (> k). right is the solution. 
        return right
