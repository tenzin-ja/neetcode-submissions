# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    '''
    Given an array of linked lists, where each list is sorted
    Return the sorted linked list that is the result of merging all of the other linked list
    So basically combine all lists into one list with all the previous lists
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        #heap solution

        heap = [] 
        
        #k log k 
        #we want to iterate through the array, getting the index
        #and the node(head of linked list)
        for i, node in enumerate(lists):
            #if node isn't none
            if node:
                #heapq uses minheap automatically
                #we need
                heapq.heappush(heap, (node.val,i,node))

        dummy = ListNode()
        cur = dummy

        #n log K
        #this is to start popping from the heap
        while heap:
            #storing the popped heap node into these variables
            val,i,node = heapq.heappop(heap)

            #popped node is the smallest node
            cur.next = node
            cur = node

            #node is to be moved, check if its an actual node
            #then push it to the heap
            node = node.next

            if node:
                heapq.heappush(heap, (node.val,i,node))
            
        return dummy.next

            #O(N log k)
            #O(k) space