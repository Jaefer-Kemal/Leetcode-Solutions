# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def inorder(root):
            if root is None:
                return []

            res = []
            res.extend(inorder(root.left))
            res.append(root.val)
            res.extend(inorder(root.right))

            return res

    
        res = inorder(root)

        def BST(res):
            if len(res) == 0:
                return None
            
            mid = len(res) // 2

            root = TreeNode(res[mid])

            root.left = BST(res[:mid])
            root.right = BST(res[mid +1 :])

            return root
        
        return BST(res)