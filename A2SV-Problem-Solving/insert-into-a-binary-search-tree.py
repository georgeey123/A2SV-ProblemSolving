# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newnode = TreeNode()

        if not root:
            root = newnode
            newnode.val = val

        # left = root.left
        # right = root.right

        if val < root.val:
            if root.left is None:
                root.left = newnode
                newnode.val = val
            self.insertIntoBST(root.left, val)
        elif val > root.val:
            if root.right is None:
                root.right = newnode
                newnode.val = val
            self.insertIntoBST(root.right, val)
        # else:
        #     root = newnode
        #     newnode.val = val 

        return root
            

