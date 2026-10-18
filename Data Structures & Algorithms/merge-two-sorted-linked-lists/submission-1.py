# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
Given two lists, merge them into one list ordered in ascending order
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #create a dummy node that will act as where our new list can begin
        dummy = ListNode()
        #this new list will begin its pointers from here
        curr = dummy

        #while neither of the lists.next are empty, continue iterating through them 
        #we want  to compare each l1 and l2, and point cur to the smaller of the two
        while (list1 and list2):
            
            #if list1.val is less than l2.val, then assign the curr node to point to l1,
            #then set curr to l1 for continuation of linked list, then move l1 forward to its next node
            if list1.val < list2.val:

                curr.next = list1
                curr = list1
                list1 = list1.next
            #This will cover the conditions of whether l1.val and l2.val are equal, or
            #l2.val < l1.val
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next

        #once we break out of the loop, set curr's final pointer to whichever list is nonempty,
        #or it'll point to None, which is also fine
        if list1: 
            curr.next = list1 
        else: 
            curr.next = list2

        return dummy.next
