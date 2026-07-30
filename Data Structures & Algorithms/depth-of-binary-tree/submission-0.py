# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #count must return a number that adds to the current number given 
        #by maxDepth
        if not root:
            return 0

        #contains the number of nodes to the left of the tree
        l = self.maxDepth(root.left) + 1
        #contain the number of nodes to the right of the tree
        r = self.maxDepth(root.right) + 1
        return max(l,r)