# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a = []
        def inorder(root):  
            if root is None:
                return
            inorder(root.left)
            a.append(root.val)
            inorder(root.right)
        inorder(root)
        print(a)
        return a[k-1] if k > 0 else a[0]

                