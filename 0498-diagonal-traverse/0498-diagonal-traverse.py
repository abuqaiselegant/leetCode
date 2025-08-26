class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        m, n = len(mat), len(mat[0])
        result = []

        d = {}
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                d.setdefault(r+c,[]).append(mat[r][c])
        
        for diag in range(n+m-1):
            if diag%2==0:
                result.extend(d[diag][::-1])
            else:
                result.extend(d[diag])
        return result



        
    
        # if not mat: return []
        
        # m, n = len(mat), len(mat[0])
        # result = []
        
        # for d in range(m + n - 1):
        #     temp = []
            
        #     # Starting row and column for this diagonal
        #     r = 0 if d < n else d - n + 1
        #     c = d if d < n else n - 1
            
        #     # Collect all elements in this diagonal
        #     while r < m and c >= 0:
        #         temp.append(mat[r][c])
        #         r += 1
        #         c -= 1
            
        #     # Reverse every alternate diagonal
        #     if d % 2 == 0:
        #         result.extend(temp[::-1])
        #     else:
        #         result.extend(temp)
        
        # return result
