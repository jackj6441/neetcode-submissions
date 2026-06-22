"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        root = Node(node.val)
        visit = {}
        visit[node] = root
        def dfs(my, node):
            for n in node.neighbors:
                if n not in visit:
                    new =  Node(n.val)
                    visit[n] = new
                    my.neighbors.append(new)
                    dfs(new, n)
                else:
                    my.neighbors.append(visit[n])
        dfs(root, node)
        return root