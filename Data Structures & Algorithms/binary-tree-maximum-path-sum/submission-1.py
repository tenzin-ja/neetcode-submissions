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
        
        #a path is defined as a sequence of adjacent nodes

        #we need to do post order: left right node
        self.max_sum = float('-inf')
        def post_order(node):
            if node is None:
                return 0
            left = max(0,post_order(node.left))
            right = max(0,post_order(node.right))

            current_sum = node.val + left + right
            self.max_sum = max(current_sum,self.max_sum)
            return node.val + max(left,right)
        
        post_order(root)
        return self.max_sum
