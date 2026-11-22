# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # swap left and right of current node 
        # then call the invert tree of the left subtree then the right subtree
        if not root or (not root.left and not root.right):
            return root

        left = root.left
        right = root.right

        # swap them 
        root.right = left
        root.left = right

        # call the recursion 
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root 
