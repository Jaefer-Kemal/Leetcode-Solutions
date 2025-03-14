# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return []
        
        stack = []
        stack.append((root, root.val))
        expected_node = None
        while stack:
            node, num = stack.pop()
            if node:
                if val == num:
                    expected_node = node
                    break
                
                elif num > val and node.left:
                    stack.append((node.left, node.left.val))
                elif num < val and node.right:
                    stack.append((node.right, node.right.val))

        
        return expected_node