# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    '''
    Given the beginning of a singly linked list head,
    reverse the list, and return the new beginning of the list
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp
            
        return prev