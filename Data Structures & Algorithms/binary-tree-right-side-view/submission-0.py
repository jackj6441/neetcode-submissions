# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        a = []
        def dfs(root, depth):
            if root is None:
                return
            if len(a) == depth:
                a.append([])
            a[depth].append(root.val)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root,0)
        print(a)
        out = []
        for i in range(len(a)):
            out.append(max(a[i]))
        return out

        