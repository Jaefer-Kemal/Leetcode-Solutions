# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = [[root.val]]
        records = []
        nodes = []

        while queue:
            node = queue.popleft()   

            if node.left:
                records.append(node.left.val)
                nodes.append(node.left)
            
            if node.right:
                records.append(node.right.val)
                nodes.append(node.right)
            
            if len(queue) == 0:
                if records:
                    res.append(records)

                for nd in nodes:
                    queue.append(nd)
                
                records = []
                nodes = []

        return res

