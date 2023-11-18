# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def search(node):
            if not node:
                return []

            return search(node.left) + [node.val] + search(node.right)

        res = search(root)
        return res[k - 1]