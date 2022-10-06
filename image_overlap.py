'''
You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.
'''

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        # help function to count overlaps in A (shifted) and B:
        def check_overlap(side_x, down_x, A, B):
            overlap_right_down = 0
            overlap_right_up = 0
            overlap_left_down = 0
            overlap_left_up = 0
            n = len(A)
            for i in range(n):
                for j in range(n):
                    if i+side_x < n and j+down_x < n:
                        overlap_right_down += A[i+side_x][j+down_x] & B[i][j]
                    if i-side_x >= 0 and j+down_x < n:
                        overlap_left_down += A[i-side_x][j+down_x] & B[i][j]
                    if i-side_x >= 0 and j-down_x >= 0:
                        overlap_left_up += A[i-side_x][j-down_x] & B[i][j]
                    if j-down_x >= 0 and i+side_x < n:
                        overlap_right_up += A[i+side_x][j-down_x] & B[i][j]
            
            return max(overlap_right_down, overlap_left_down, overlap_right_up, overlap_left_up)
        
        # try all options:
        max_overlap = 0
        for i in range(len(A)):
            for j in range(len(A)):
                max_overlap = max(max_overlap, check_overlap(i, j, A, B))
                
        return max_overlap
