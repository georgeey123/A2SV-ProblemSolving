# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        _list = []

        def bfs(node):            
            if not node:
                return

            queue = deque([node])

            while queue:

                boundary = len(queue)
                cur_level = []

                for _ in range(boundary):
                    node = queue.popleft()
                    cur_level.append(node.val)

                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)

                _list.append(cur_level)

        bfs(root)
        
        averages = []

        for i in range(len(_list)):
            level = i
            average = sum(_list[i]) / len(_list[i])

            averages.append(average)

        return averages



