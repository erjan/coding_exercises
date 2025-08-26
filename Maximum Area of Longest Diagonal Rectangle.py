You are given a 2D 0-indexed integer array dimensions.

For all indices i, 0 <= i < dimensions.length, dimensions[i][0] represents the length and dimensions[i][1] represents the width of the rectangle i.

Return the area of the rectangle having the longest diagonal. If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the maximum area.

  ------------------------------------------------------------------------------------------------

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxdiag = 0
        maxres = 0

        print(dimensions)
        for i in range(len(dimensions)):
            w,h = dimensions[i]


            diag = (w*w + h*h)**0.5
            cur_res = w*h

            dimensions[i].extend([diag,cur_res])
        

        dimensions.sort(key = lambda x: (x[2], x[3]))

        res = dimensions[-1][3]

        return res

--------------------------------------------------

#other solution

class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        max_area, max_diag = 0, 0

        for l, w in dimensions:
            curr_diag = l * l + w * w
            if curr_diag > max_diag or (curr_diag == max_diag and l * w > max_area):
                max_diag = curr_diag
                max_area = l * w

        return max_area
