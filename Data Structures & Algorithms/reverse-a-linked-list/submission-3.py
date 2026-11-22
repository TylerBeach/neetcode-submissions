# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       # 0 1 2 3 
#      p C 
        prev = None
        curr = head 
        while curr and curr.next:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        if curr:
            curr.next = prev
        return curr