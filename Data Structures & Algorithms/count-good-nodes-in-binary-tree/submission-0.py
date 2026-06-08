# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def help(root, mx):
            if root is None:
                return
            if root.val >= mx:
                self.count += 1
                mx = root.val
            
            help(root.left, mx)
            help(root.right,mx)
        help(root, float('-inf'))
        return self.count