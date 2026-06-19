class TreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            i = ord(w) - ord('a')
            if cur.children[i] is None:
                cur.children[i] = TreeNode()
            cur = cur.children[i]
        cur.endOfWord = True
    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            i = ord(w) - ord('a')
            if cur.children[i] is None:
                return False
            cur = cur.children[i]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            i = ord(w) - ord('a')
            if cur.children[i] is None:
                return False
            cur = cur.children[i]
        return True
        
        