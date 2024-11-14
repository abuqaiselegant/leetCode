class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """n=3
        rows,cols = [0]*n,[0]*n
        d1,d2 = 0,0
        player = 1
        for r,c in moves:
            rows[r]+=player
            cols[c]+=player
            if r==c :
                d1+=player
            if r+c==n-1:
                d2+=player
            if abs(rows[r])==n or abs(cols[c])==n or abs(d1)==n or abs(d2)==n:
                if player ==1:
                    return "A"
                else:
                    return "B"
            player*=-1
        if len(moves)==(n*n):
            return "Draw"
        else:
            return "Pending"""
        board =[[0]*3 for i in range(3)]
    
        for i in range(len(moves)):
            row = moves[i][0]
            col = moves[i][1]
        
            if i%2==0:
                board[row][col]=1
            else:
                board[row][col]=-1

        diagonal1_sum =0
        diagonal2_sum =0
        for i in range(3):
            if sum(board[i])==3: return "A"
            if sum(board[i])==-3: return "B"
        
            col_sum = board[0][i]+board[1][i]+board[2][i]
            if col_sum == 3:
                return "A"
            if col_sum ==-3:
                return "B"
            diagonal1_sum += board[i][i]
            if diagonal1_sum ==3:
                return "A"
            if diagonal1_sum ==-3:
                return "B"
            diagonal2_sum +=board[i][2-i]
            if diagonal2_sum==3:
                return "A"
            if diagonal2_sum==-3:
                return "B"
        if len(moves)==9:
            return "Draw"
        return "Pending"
