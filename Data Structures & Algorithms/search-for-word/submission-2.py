class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        words = []
        w,h = len(board[0]),len(board)
        def dfs(cur,i,j):
            
            if cur == len(word):
                return True
            if i >= h or i < 0 or j >= w or j < 0:
                return False
            if board[i][j] == word[cur]:
                tmp =  board[i][j]
                board[i][j] = '#'
                cur += 1
                result = (dfs(cur, i+1, j) or
                dfs(cur, i-1, j) or 
                dfs(cur, i, j+1) or
                dfs(cur, i, j-1))
                board[i][j] = tmp
                return  result

        for i in range(h):
            for j in range(w):
                if dfs(0,i,j):
                    return True
        return False
        
            

            
