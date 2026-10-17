# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    '''
    Given the heads of two sorted linked lists, 
    merge the two lists into one sorted linked list, and return the head of the mereged list
    '''
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:     
        
        #dummy node to basically iterate throughout the two linked lists
        d = ListNode()
        cur = d

        while list1 and list2:
            #checking if l1 has the smaller value
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            #this means that either list2 has the smaller number
            #or they are equal, which in that case it doesn't matter
            #which node we set cur to
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
        
        cur.next = list1 if list1 else list2

        return d.next