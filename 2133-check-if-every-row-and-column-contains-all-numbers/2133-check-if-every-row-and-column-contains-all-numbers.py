class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        mylist = [x for x in range(1,len(matrix)+1)]
        # print(mylist)
        for rows in matrix:
            if set(rows) != set(mylist):
                return False
        # print(rows)
        
        for c in range(len(matrix)):
            col = [matrix[r][c] for r in range(len(matrix))]
            if set(col) !=set(mylist):
                return False
            # print(col)
        return True
