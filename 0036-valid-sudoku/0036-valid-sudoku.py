class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set() for i in range(9)]
        column =[set() for j in range(9)]
        box = [set() for k in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num ==".":
                    continue
                if num in row[i]:
                    return False
                row[i].add(num)

                if num in column[j]:
                    return False
                column[j].add(num)

                box_index = (i//3)*3+(j//3)
                if num in box[box_index]:
                    return False
                box[box_index].add(num)
        return True