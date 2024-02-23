# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        
        def dp(node):
            if node in memo:
                return node
            
            if not node:
                return [0,0]
            
            left = dp(node.left)
            right = dp(node.right)
            
            pick = node.val + left[1] + right[1]
            dont_pick = max(left) + max(right)
            
            memo[node] = [pick, dont_pick]
            return memo[node]
            
        return max(dp(root))
            