# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    '''
    Given the head of a singly linked list
    reorder the linked list to the indexed list given 
    '''
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #create two pointers to scan through the list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        prev = None
        curr = second_half

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2