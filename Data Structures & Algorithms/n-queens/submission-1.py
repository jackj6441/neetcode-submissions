class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def safe(b, i, j):
            for z in range(n):
                if b[i][z] == 'Q':
                    return False
                elif b[z][j] == 'Q':
                    return False
                x1 = i-z
                y1 = j-z
                if x1 >= 0 and x1 < n and y1 >= 0 and y1 < n:
                    if b[x1][y1] == 'Q':
                        return False
                x1 = i-z
                y1 = j+z
                if x1 >= 0 and x1 < n and y1 >= 0 and y1 < n:
                    if b[x1][y1] == 'Q':
                        return False
            return True
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        def dfs(s):
            nonlocal res
            if s >= n:
                res.append(["".join(row) for row in board])
                return
            for i in range(0, n):
                if safe(board, s, i):
                    board[s][i] = 'Q'
                    dfs(s+1)
                    board[s][i] = '.'
        dfs(0)
        return res
                
                

            