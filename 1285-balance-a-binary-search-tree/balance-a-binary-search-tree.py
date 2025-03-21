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

            return inorder(root.left) + [root.val] + inorder(root.right)

    
        sorted_vals = inorder(root)

        def BuildBST(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2

            root = TreeNode(sorted_vals[mid])

            root.left = BuildBST(left , mid - 1)
            root.right = BuildBST(mid + 1, right)

            return root
        
        return BuildBST(0, len(sorted_vals) - 1)