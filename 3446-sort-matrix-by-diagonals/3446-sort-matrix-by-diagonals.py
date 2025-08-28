class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        a = {}
        for i in range(len(grid)):
            for j in range(len(grid)):
                a.setdefault(i-j,[]).append(grid[i][j])

        for i in a:
            if i >=0:
                a[i].sort(reverse =True)
            else:
                a[i].sort()
        
        for r in range(len(grid)):
            for c in range(len(grid)):
                grid[r][c] = a[r-c].pop(0)
        return grid