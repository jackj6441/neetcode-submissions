# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a = []
        def bfs(root):
            if root is None:
                return []
            q = []
            q.append(root)
            while q:
                count = len(q)
                for i in range(count):
                    cur = q.pop()
                    a.append(cur.val)
                    if cur.right: q.append(cur.right)
                    if cur.left: q.append(cur.left)
        bfs(root)
        a.sort()
        return a[k-1] if k > 0 else a[0]

                