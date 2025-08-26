import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        x=0
        y=0
        max_diag = 0
        max_area = 0
    
        for i in dimensions:
            diag = i[0]*i[0]+i[1]*i[1]
            area = i[0]*i[1]
           
            if diag >max_diag or (diag ==max_diag and area>max_area):
                max_diag = diag
                max_area =area
        return max_area
