# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    '''
    Given the root of a bst and an int k,
    return the kth smallest value in the tree
    '''
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #we basically want to go through the tree until we find the 
        #node with the kth smallest number

        #to do this we would need to travse the tree in a in order traversal

        self.count = k
        self.ans = 0

        def helper_func(root):
            if root is None:
                return            
            
            helper_func(root.left)

            #we know we're at k when count = 1 since
            #we're counting downwards. since this is 0 indexed, 
            #we stop at 1 instead of 0
            if self.count == 1:
                self.ans = root.val
            
            self.count = self.count - 1
            
            #this helps us breakout, since if the node we're at is 
            #the kth node, the recursion will end here. however recrusion will still continue,
            #it just wont go into the right trees
            if self.count > 0:
                helper_func(root.right)
        
        helper_func(root)

        return self.ans