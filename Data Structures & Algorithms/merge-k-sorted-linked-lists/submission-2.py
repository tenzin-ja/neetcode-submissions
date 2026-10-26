# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

'''
Given an array of k linked lists
return the sorted linked list taht is the result of merging all 
linked lists
'''
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        #the idea here is to use a heap to sort the 
        #pointers to the current node we are at for 
        #each of the individual linked lists, using the heap,
        #we can pop the smallest value node, and add it to our new linked list

        heap = []

        for i, node in enumerate(lists):
            #this is checking if the linked list is empty
            if node:
                #we want the val to be the compared, i as a tiebreaker, and node is what'll 
                #be inside the heap
                heapq.heappush(heap,(node.val,i,node))
            
        #now that we have our heap, we want to iterate through it
        #when we reach a lowest node, we pop it from the heap,
        #then add it to our new list
        dummy = ListNode()
        curr = dummy
        
        #iterate through heap
        while heap:

            #pop the lowest value node
            val,i,node = heapq.heappop(heap)
            
            #set the next pointer to the popped node, 
            #then we want to set the curr to the new node
            curr.next = node
            curr = node
            
            node = node.next

            #this is checking if node.next would be None
            #in which case we wouldn't add to heap
            if node:
                heapq.heappush(heap, (node.val,i,node))
                
        return dummy.next