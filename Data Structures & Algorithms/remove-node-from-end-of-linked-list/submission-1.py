# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    '''
    Given a head of a linked list and an int n
    remove the nth node from the end of the list and return its head
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        #idea here is to use two pointers. in order to do this in one pass,
        #we want to have first move at an n headstart of slow
        first = head

        #we use a dummy node, so that instead of second landing on target,
        #it lands at one before it, so that we can break the connection without 
        #using a prev variable.
        dummy = ListNode()
        dummy.next = head
        second = dummy

        #headstart for first
        for i in range(n):
            first = first.next

        #continue the iteration if first is not already none
        while first:
            second = second.next
            first = first.next

        #now that first has reached the end of the list, we can just 
        #rewire the connection of second, so that it skips the target node
        
        second.next = second.next.next
        
        #we want to return dummy.next here instead of head,
        #because returning head could return the node we meant to delete,
        #if the head was the target node
        return dummy.next
            
            
