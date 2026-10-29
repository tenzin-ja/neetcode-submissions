# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    Given two lists,
    create a tree from the travesal orders
    return the root
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

        #we want to first create a hashmap out of the in order traversal
        #this will be used for 
        in_order = {val: idx for idx,val in enumerate(inorder)}

        #this will be to track which node we're on
        pre_idx = [0]

        #now we need to do our recursive loop
        def helper_func(l,r):
            
            #this means the l and r cross, meaning that there is no node at this point
            if l > r:
                return None

            #this lets us know what value we're looking for
            root_val = preorder[pre_idx[0]]
            #count everytime we do recursion
            pre_idx[0] += 1
            #wrap this into a treenode so it matches buildtree return requirement
            root = TreeNode(root_val)

            #now we move onto the recursive step
            root.left = helper_func(l, in_order[root_val] - 1)
            root.right = helper_func(in_order[root_val] + 1, r)

            return root
        return helper_func(0,len(preorder)-1)