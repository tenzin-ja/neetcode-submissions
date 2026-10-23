# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    '''
    Given the head of a linked list
    fix the list so that it follows the given order
    '''
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        #main idea here is to use a fast and slow pointer
        #use them to find the middle of the list, then split

        slow = head
        fast = head
        #general slow and fast logic
        while fast and fast.next: 
        
            slow = slow.next
            fast = fast.next.next
        
        #now that we have slow.next = the middle of the list
        #we want to split it at the mid so that we can reverse the ending of the list
        mid = slow.next
        #we want to disconnect the first half from the second half, so that we can reverse 
        #the second half list
        slow.next = None
        prev = None 

        #normal reverse algorithm
        while mid != None: 
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        
        #now that the second half is reversed, we can build the final linked list
        #we set first to the head of the first half, and second to the head of the second
        #half
        first = head
        second = prev
        
        #we want to loop until the end of the second list since it'll be 
        #equal to or longer then the first half
        while second:
            '''
            The main idea here is that we want loop through both lists,
            setting each node in the first list to a node in the second list.
            Then resetting first and second to their og .next, and continuing 
            the cycle.
            '''
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        