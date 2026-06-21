class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        cur = root
        for w in words:
            for l in w:
                if l not in cur.children:
                    cur.children[l] = TrieNode()
                cur = cur.children[l]
            cur.word = w
            cur = root
        res = []
        h, w = len(board), len(board[0])
        cur = ''
        def dfs(i,j,node):
            nonlocal cur
           
            if i< 0 or i >= h or j< 0 or j >= w:
                return
            ch = board[i][j]
            if ch not in node.children:
                return
            node = node.children[ch]

            if node.word is not None:
                res.append(node.word)
                node.word = None
                
            tmp = board[i][j]
            board[i][j] = '#'
            dfs(i+1,j,node)
            dfs(i,j+1,node)
            dfs(i-1,j,node)
            dfs(i,j-1,node)
            board[i][j] = tmp
        for i in range(h):
            for j in range(w):
                dfs(i, j, root)
        return res