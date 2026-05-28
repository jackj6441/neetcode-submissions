class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        a = []
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == ".":
                    continue
                else:
                    for n in range(9):
                        if board[i][n] == cur and n != j:
                            return False
                            print(f1)
                        if board[n][j] == cur and n != i:
                            return False
                            print(f2)

                    start_r = (i//3)*3
                    start_c = (j//3)*3
                    for r in range(start_r,start_r+3):
                        for c in range(start_c,start_c+3):
                            if (r != i or c != j) and board[i][j] == board[r][c]:
                                return False
                                print(f3)
                            
        return True