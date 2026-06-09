# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def getMax(root):
            if root is None:
                return 0
            cur = root.val + max(getMax(root.left),getMax(root.right))
            return max(0, cur)
        best = float('-inf')
        def dfs(root):
            nonlocal best
            if root is None:
                return float('-inf')
            cur = root.val + getMax(root.right) + getMax(root.left)
            best = max(best, cur)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return best
            