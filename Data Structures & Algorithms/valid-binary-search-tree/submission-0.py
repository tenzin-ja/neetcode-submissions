# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
Given the root of a binary tree
return true if its a valid binary search tree
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        #idea here is to do a dfs through the tree, determine if the 
        #left node is smaller than the root and the right node is 
        #greater than the root
        def helperfunc(root,max_val,min_val):
            if not root:
                return True
            if root.val >= max_val or root.val <= min_val:
                return False
            return helperfunc(root.right,max_val,root.val) and helperfunc(root.left,root.val,min_val)
        
        return helperfunc(root,float('inf'),float('-inf'))
        