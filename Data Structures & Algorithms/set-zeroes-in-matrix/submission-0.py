class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_m = {}
        col_m = {}
        h, w = len(matrix),len(matrix[0])
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    row_m[i] = True
                    col_m[j] = True
        for i in range(h):
            for j in range(w):
                if i in row_m or j in col_m:
                    matrix[i][j] = 0

                
        
                
        