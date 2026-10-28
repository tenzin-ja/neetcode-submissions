# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Given a binary tree, return level order traversal(bfs)
and return a list containing sublist of each level
'''


from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #if the tree is empty, we can just return an empty list
        #this is because queue will still append None
        if root is None:
            return []
        #create queue for bfs traversal, add root for intial iteration
        queue = deque()
        queue.append(root)
        #this will contain the actual sublists
        ans = []

        while queue:
            
            #this is for the level traversal
            n = len(queue)
            level = []
            for i in range(n):
                          
                node = queue.popleft()
                #this is to add the current levels nodes to the sublists
                level.append(node.val)     
                #this is for adding the left and right node to the queue
                #make sure order is correct
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            ans.append(level)
        
        return ans
            