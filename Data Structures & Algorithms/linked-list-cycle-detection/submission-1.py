# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    '''
    Given the beginning of a linked list
    return true if there is a cycle in the list,
    otherwise return false

    cycle is defined as a node that points to a previous node in the list
    '''
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        dummy = ListNode()
        dummy.next = head

        slow = dummy
        fast = dummy

        #We are only worried if fast will reach an end node, 
        #since fast will be ahead of slow. this makes sure
        #fast.next.next doesn't fail
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False





