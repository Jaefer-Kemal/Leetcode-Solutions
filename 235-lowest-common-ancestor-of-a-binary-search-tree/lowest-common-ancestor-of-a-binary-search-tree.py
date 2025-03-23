# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def findPath(root, val):
            if root is None:
                return []
            
            if root.val == val:
                return [root]
            
            if root.val > val:
                left_path = findPath(root.left, val)
                if left_path:
                    return [root] + left_path
            else:
                right_path = findPath(root.right, val)
                if right_path:
                    return [root] + right_path
            
            return []

        p_ancestor = findPath(root,p.val)
        q_ancestor = findPath(root,q.val)

        if len(p_ancestor) > len(q_ancestor):
            path_set = set(p_ancestor)
            smaller_path = q_ancestor
            index = len(smaller_path) - 1
        else:
            path_set = set(q_ancestor)
            smaller_path = p_ancestor
            index = len(smaller_path) - 1 

        while index >= 0:
            if smaller_path[index] in path_set:
                return smaller_path[index]
            
            index -= 1