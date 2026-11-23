# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        list1_curr = list1
        list2_curr = list2
        dummy = ListNode()
        dummy_head = dummy
        
        while list1_curr and list2_curr:
            if list1_curr.val <= list2_curr.val:
                # add list1 to dummy 
                dummy.next = list1_curr
                list1_curr = list1_curr.next
            else:
                dummy.next = list2_curr
                list2_curr = list2_curr.next
            dummy = dummy.next

        # left overs in either of them 

        if list1_curr:
            dummy.next = list1_curr
        if list2_curr: 
            dummy.next = list2_curr

        return dummy_head.next


        