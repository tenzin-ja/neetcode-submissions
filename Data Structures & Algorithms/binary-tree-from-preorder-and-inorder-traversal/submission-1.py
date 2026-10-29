# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    '''
    Given two integer arrays
    Preorder and inorder

    build the binary tree from the two ways and return its
    root
    '''

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        #creates a hashmap with the val to idx from inorder list
        #this is to avoid scanning through inorder. with this we just have
        #O(1) lookup
        in_order_hm = {val:idx for idx, val in enumerate(inorder)}

        #using a list so its used as a global variable.
        #this will be used to move through the pre order list
        pre_order_idx = [0]

        #helper function to determine the root of the binary tree
        def arr_to_tree(l,r):
            
            #if the numbers "cross" each other, that means we've found 
            #where an empty node will be.
            if l > r: return None
            
            root_val = preorder[pre_order_idx[0]]
            pre_order_idx[0] += 1
            root = TreeNode(root_val)
            
            #we recurse with either l,r and its location in the in_order list
            #this helps us determine when the l,r values cross each other
            root.left = arr_to_tree(l, in_order_hm[root_val] - 1)
            root.right = arr_to_tree(in_order_hm[root_val] + 1, r)

            return root
        
        return arr_to_tree(0,len(preorder)-1) 