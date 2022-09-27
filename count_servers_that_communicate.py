
'''
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.
'''

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # Check the input: size of the grid. If it is 0 then exit
        if not (cols and rows):
            return 0

        connected = 0                  # store number of connected computers                 
        points=[]                      # store coordinates of all the computers 
        comps_per_row = [0] * rows     # store number of computers in given row
        comps_per_col = [0] * cols     # store number of computers in given column
        
        for row_i in range(rows):
            for col_i in range(cols):
                if grid[row_i][col_i]:              # checking if given cell is not 0
                    points.append((row_i,col_i))    # add coordinated to the set
                    comps_per_row[row_i]+=1         # increase nimber of computers in a given row
                    comps_per_col[col_i]+=1         # increase nimber of computers in a given column 
        
        # iterate through all computers
        for row_i,col_i in points:
            # is there more than 1 computer in given row or column
            if comps_per_row[row_i]>1 or comps_per_col[col_i]>1 :
                # if yes, then computer is connected, count him      
                connected += 1                      
        
        return connected
