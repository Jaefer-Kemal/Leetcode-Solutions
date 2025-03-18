# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def inorder(root):
            if root is None:
                return []
            result = []
            left = inorder(root.left)
            result.extend(left)
            result.append(root.val)
            right = inorder(root.right)
            result.extend(right)

            return result

            
        arr =  inorder(root)
        return arr[k-1]

