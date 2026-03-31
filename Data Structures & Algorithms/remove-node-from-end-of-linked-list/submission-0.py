# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy, pt1, pt2 = head, head, head
        prev = None
        while n > 0:
            pt2 = pt2.next
            n -= 1
        while pt2:
            prev = pt1
            pt1 = pt1.next
            pt2 = pt2.next
        if not prev:
            return dummy.next
        prev.next = pt1.next
        return dummy