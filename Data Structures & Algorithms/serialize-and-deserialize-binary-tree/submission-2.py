# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    '''
    convert an in memory structure into a sequence of bits 
    Take in a tree
    return an encoded string
    '''
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append('N')
                return 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        #this is to seperate each list item with ','
        return ','.join(res)
    '''
    Taking in an encoded string
    returning a treeNode
    '''
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        data = data.split(',')
        #this helps us iterate through the data
        vals = iter(data)

        def dfs():
            val = next(vals)
            if val == 'N':
                return None
            
            node = TreeNode(int(val))
            
            #this works because we are returning the node itself
            #we are basically doing the same order as the preorder 
            #traversal, so that we get the same tree
            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()