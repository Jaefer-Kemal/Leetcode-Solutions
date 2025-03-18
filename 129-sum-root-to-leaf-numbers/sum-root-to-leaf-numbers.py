# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root, total):

            if root.left is None and root.right is None:
                return [total * 10 + root.val]
            
            result = []

            if root.left:
                result.extend(dfs(root.left, total * 10 + root.val))
            
            if root.right:
                result.extend(dfs(root.right, total * 10 + root.val))

            return result

        result = dfs(root, 0)

        return sum(result)