class Solution:
    def solve(self, board: List[List[str]]) -> None:
        track = []
        q = deque()
        h,w = len(board),len(board[0])
        for i in range(h):
            if board[i][0] == 'O':
                q.append((i,0))
                track.append([i,0])
            if board[i][w-1] == 'O':
                q.append((i,w-1))
                track.append([i,w-1])
        for j in range(w):
            if board[0][j] == 'O':
                q.append((0,j))
                track.append([0,j])
            if board[h-1][j] == 'O':
                q.append((h-1,j))
                track.append([h-1,j])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        print(track)
        while q:
            i, j = q.popleft()
            for dx, dy in dirs:
                if i+dx < 0 or i+dx >= h or j+dy < 0 or j+dy >= w:
                    continue
                if [i+dx,j+dy] in track or board[i+dx][j+dy] == 'X':
                    continue
                q.append((i+dx,j+dy))
                track.append([i+dx,j+dy])
        print(track)
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O' and [i,j] not in track:
                    board[i][j] = 'X'
                