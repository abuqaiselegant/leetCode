class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        sum2 =0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i==j and i+j!=len(mat)-1:
                    sum+=mat[i][j]
                if i+j == len(mat)-1:
                    sum2+=mat[i][j]
        sum =sum+sum2
        return sum