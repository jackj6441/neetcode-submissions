class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        h, w = len(matrix),len(matrix[0])
        res = []
        m = {}
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        def loop(i,j,di):
            res.append(matrix[i][j])
            m[(i,j)] = True
            dx, dy = dirs[di]
            next_i, next_j = i + dx, j + dy
            if 0 <= next_i < h and 0 <= next_j < w and (next_i, next_j) not in m:
        # 没撞墙，保持当前方向 di 继续走
                loop(next_i, next_j, di)
            else:
        # 撞墙了！顺时针转弯：(di + 1) % 4
                next_di = (di + 1) % 4
                dx, dy = dirs[next_di]
                next_i, next_j = i + dx, j + dy
        
        # 转弯后如果还是安全的，就继续走；如果转弯后也走不通，说明全走完了，直接结束
            if 0 <= next_i < h and 0 <= next_j < w and (next_i, next_j) not in m:
                loop(next_i, next_j, next_di)
        loop(0,0,0)
        return res
