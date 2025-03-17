# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(root, minimum, maximum):
            if root is None:
                return maximum - minimum

            minimum = min(minimum, root.val)
            maximum = max(maximum, root.val)
            
            left_res = dfs(root.left, minimum, maximum)
            right_res = dfs(root.right, minimum, maximum)

            return max(left_res, right_res)
        
        return max(dfs(root.left, root.val, root.val), dfs(root.right, root.val, root.val))