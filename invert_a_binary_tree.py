"""
this was super easy haha. 
I was inspired to solve this when I remembered watching
Ben Awad and Clement Mihailscu's video on reversing a linked list 
and inverting a binary tree. The last few minutes were so funny lololol.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # recursion? 
        if root is not None:
            left = root.left
            right = root.right
            root.left = right
            root.right = left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

