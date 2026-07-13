class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        h, w = len(matrix),len(matrix[0])
        rows, cols = [False] * h, [False] * w
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        for i in range(h):
            for j in range(w):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0

                
        
                
        