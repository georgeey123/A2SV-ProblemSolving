# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        left_tree = root.left
        right_tree = root.right

        def mirror(left, right):
            if not left and not right:
                return True
            if (not left or not right) or (left.val != right.val):
                return False
            
            inner_symmetry = mirror(left.right, right.left)
            outer_symmetry = mirror(left.left, right.right) 

            return inner_symmetry and outer_symmetry
        return mirror(left_tree, right_tree)