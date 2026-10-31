# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    given the root of a binary tree
    return the max path sum of any path
    '''
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        #this is to account for negative tree edge case
        #with negative trees, this allows us to find the smallest 
        #negative number, because of our current_sum calculation
        self.max_sum = float('-inf')

        #we need to do post order: left right node
        def post_order(node):

            #if we reach an empty node, just return 0
            if node is None:
                return 0
            
            #we want only non negative paths, which is why we determine between 
            #0 and the max node
            left = max(0,post_order(node.left))
            right = max(0,post_order(node.right))

            #calculate the current sum using the current node
            current_sum = node.val + left + right
            #determine if its larger then our current max
            self.max_sum = max(current_sum,self.max_sum)
            #return back up the node value with the max of the left and right,
            #to avoid sending paths with both left and right values
            return node.val + max(left,right)
        
        post_order(root)
        return self.max_sum
