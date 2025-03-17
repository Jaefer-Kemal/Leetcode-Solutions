# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        level = 0
        queue = deque([root])
        res = []
        while queue:
            store = []
            for i in range(len(queue)):
                node = queue.popleft()
                store.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 != 0:
                store = store[ : : -1]
            
            res.append(store)
            level += 1
        
        return res