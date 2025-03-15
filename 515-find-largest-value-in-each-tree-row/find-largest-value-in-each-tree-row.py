# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []

        queue = deque()
        queue.append(root)

        maximum = float("-inf")
        rem = []
        while queue:
            front = queue.popleft()

            maximum = max(maximum, front.val)
            rem.append(front)
            
            if not queue: 
                res.append(maximum)
                maximum = float("-inf")

                while rem:
                    node = rem.pop()

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

        return res
        