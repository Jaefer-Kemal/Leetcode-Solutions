# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = deque([root])

        level = 0

        while queue:
            # used to store odd level node
            store = []
            for i in range(len(queue)):
                node = queue.popleft()
                if level % 2 != 0:
                    store.append(node)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if store:
                left = 0
                right = len(store) - 1
                while left <= right:
                    left_node = store[left]
                    right_node = store[right]
                    
                    left_node.val, right_node.val = right_node.val, left_node.val

                    left += 1
                    right -= 1
            
            level += 1

        return root
