class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix),len(matrix[0])

        top, bot = 0, rows-1
        while top<=bot:
            row = (top+bot)//2
            if target>matrix[row][-1]:
                top = row+1
            elif target<matrix[row][0]:
                bot = row-1
            else:
                break
        
        if not (top<=bot):
            return False
        row = (top+bot)//2
        
        start, end=0, cols-1
        while start<=end:
            mid = (start+end)//2
            if target>matrix[row][mid]:
                start=mid+1
            elif target < matrix[row][mid]:
                end = mid-1
            else:
                return True
        return False