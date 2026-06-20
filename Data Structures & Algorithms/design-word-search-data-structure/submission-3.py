class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            i = ord(w)-ord('a')
            if cur.children[i] is None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            
            if i >= len(word):
                return node.end
            print(node, i, word[i])
            c = word[i]
            if c == '.':
                for n in node.children:
                    if n is not None and dfs(n, i+1):
                        return True
                return False
            elif node.children[ord(c)-ord('a')] is not None:
                return dfs(node.children[ord(c)-ord('a')], i+1)
            return False
        return dfs(self.root, 0)

            
            
