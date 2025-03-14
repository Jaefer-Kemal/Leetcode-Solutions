# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root.left and not root.right:
            return True

        left = []
        right = []

        left.append(root.left)
        right.append(root.right)

        while left and right:
            l = left.pop()
            r = right.pop() 

            if l is None and r is None:
                continue

            if (l is None and r) or (r is None and l) or l.val != r.val:
                return False

            if l:
                left.append(l.left)
                left.append(l.right)
            if r:
                right.append(r.right)
                right.append(r.left)

        return True
