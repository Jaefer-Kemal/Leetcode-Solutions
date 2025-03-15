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
            if front:
                maximum = max(maximum, front.val)
                rem.append(front)
            
            if not queue:
                if maximum !=  float("-inf"):
                    res.append(maximum)
                    maximum = float("-inf")
                while rem:
                    node = rem.pop()
                    queue.append(node.left)
                    queue.append(node.right)

        return res
        