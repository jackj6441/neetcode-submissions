class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        h,w = len(board),len(board[0])
        for i in range(h):
            if board[i][0] == 'O':
                q.append((i,0))
            if board[i][w-1] == 'O':
                q.append((i,w-1))
        for j in range(w):
            if board[0][j] == 'O':
                q.append((0,j))
                
            if board[h-1][j] == 'O':
                q.append((h-1,j))
                
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            i, j = q.popleft()
            board[i][j] = 'T'
            for dx, dy in dirs:
                if i+dx < 0 or i+dx >= h or j+dy < 0 or j+dy >= w:
                    continue
                if board[i+dx][j+dy] == 'X' or board[i+dx][j+dy] == 'T':
                    continue
                q.append((i+dx,j+dy))
        print(board)
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] =='T':
                     board[i][j] = 'O'
                