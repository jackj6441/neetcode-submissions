# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preS = []
        def preOrder(root):
            if root is None:
                preS.append('#')
                return 
            preS.append (str(root.val))
            preOrder(root.left)
            preOrder(root.right)

        preOrder(root)
        print(",".join(preS))
        return ",".join(preS) 

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        r = TreeNode()
        self.i = 0
        def dfs(root):
            if vals[self.i] == '#' :
                self.i+=1
                return None
            
            
            root = TreeNode(vals[self.i])
            self.i+=1
            root.left = dfs(TreeNode())
            root.right = dfs(TreeNode())
            return root
        return dfs(r)
            




