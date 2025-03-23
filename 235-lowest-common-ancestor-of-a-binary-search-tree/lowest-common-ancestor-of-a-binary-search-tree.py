# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def BST(root, val,res):
            if root is None:
                return []

            res.append(root)

            if root.val == val:
                return res

            elif root.val > val:
                res.extend(BST(root.left, val,res))
            else:
                res.extend(BST(root.right, val,res))
            
            return res

        p_ancestor = BST(root,p.val,[])
        q_ancestor = BST(root,q.val,[])

        if len(p_ancestor) > len(q_ancestor):
            check = set(p_ancestor)
            large = q_ancestor
            n = len(large) - 1
        else:
            check = set(q_ancestor)
            large = p_ancestor
            n = len(large) - 1 

        while n >= 0:
            if large[n] in check:
                return large[n]
            
            n -= 1
