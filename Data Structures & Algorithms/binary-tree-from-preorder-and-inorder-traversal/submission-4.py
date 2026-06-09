# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        m = {val:idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0
        def dfs(l,r):
            if l > r:
                return None
            
            cur = TreeNode(preorder[self.pre_idx])
            mid = m[preorder[self.pre_idx]]
            self.pre_idx += 1

            cur.left = dfs(l, mid-1)
            cur.right = dfs(mid+1, r)

            return cur
        return dfs(0, len(preorder)-1)


        