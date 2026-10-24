# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    '''
    given the head of a linked list and an int n, remove the nth node
    return head
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        #divide this into three subparts
        #get target, remove target, set new linked list
    
        #we need to first find the target node
        fast = head

        #use a dummy node to find the target in one pass
        dummy = ListNode()
        slow = dummy
        dummy.next = head

        #fast gets a headstart depending on size of n

        for i in range(n):
            fast = fast.next

        #now we want to get the node before target
        while fast:
            slow = slow.next
            fast = fast.next

        #slow is now behind the target, we want to cut the connection
        slow.next = slow.next.next

        return dummy.next

