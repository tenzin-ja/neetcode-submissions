# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    '''
    Given the roots of two binary trees
    return true if there is a subtree of root with the same structure and node values of 
    subroot, and false otherwise
    '''  
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        #use dfs to go through left and right subtrees of the root
        #comparing them to the subroot tree
        def sameTree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            return sameTree(p.left,q.left) and sameTree(p.right,q.right)
        

        def has_subtree(root):

            if not root:
                return False
            
            if sameTree(root,subRoot):
                return True
            
            return has_subtree(root.left) or has_subtree(root.right)
        
        return has_subtree(root)