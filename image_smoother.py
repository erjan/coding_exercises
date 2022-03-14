'''
An image smoother is a filter of the size 3 x 3 that 
can be applied to each cell of an image by rounding down the average of the cell and the eight 
surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the 
surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).
'''

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        results = []

        rows = len(img)
        cols = len(img[0])

        for r, row in enumerate(img):

            results.append([])

            for c, col in enumerate(row):
                s = 0
                count = 0
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        if 0 <= (r + dx) < rows and 0 <= (c+dy) < cols:
                            s += img[r+dx][c+dy]
                            count+=1
                results[-1].append(s//count)
        return results
