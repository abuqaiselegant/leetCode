class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        height = [0] * n
        res = 0
        
        for i in range(m):
            # update histogram heights
            for j in range(n):
                if mat[i][j] == 1:
                    height[j] += 1
                else:
                    height[j] = 0
            
            # count submatrices ending at this row
            for j in range(n):
                if height[j] > 0:
                    min_h = height[j]
                    for k in range(j, -1, -1):  # go leftwards
                        if height[k] == 0:
                            break
                        min_h = min(min_h, height[k])
                        res += min_h
        return res    