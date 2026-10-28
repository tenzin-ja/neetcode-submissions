# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    '''
    Given the roots of two trees,
    determine if the tree contains the subtree
    '''
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        #we want two helper functions here, one to determine 
        #if the node contains the subtree
        #and another to move through the tree

        def is_same(p,q):
            
            #if both nodes are empty
            if not p and not q:
                return True
            #this assumes only one of them are None since first condition failed
            if not p or not q:
                return False
            #if the nodes aren't the same vals
            if p.val != q.val:
                return False
            
            #otherwise, we want to continue through the tree
            #until we reach the end of each branch
            return is_same(p.left,q.left) and is_same(p.right,q.right)
        
        #we basically want to move through the tree until 
        #we reach the end of the tree. subtree stays the same
        def moving(root,subRoot):

            #if we reach the end of the tree then we can assume it doesn't match
            if not root:
                return False
            #if is_same returns True, then the tree contains the subtree
            if is_same(root,subRoot):
                return True
            #if either left or right of the tree returns true, return true         
            return moving(root.left,subRoot) or moving(root.right,subRoot)


        
        return moving(root,subRoot)