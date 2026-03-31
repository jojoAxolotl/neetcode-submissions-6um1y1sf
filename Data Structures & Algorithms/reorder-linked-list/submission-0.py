# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. Find the middle of the list
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        second_half = slow.next
        slow.next = None

        # 2. Reverse the second half
        prev = None
        cur = second_half
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # prev is the head of the second half

        # 3. Merge the two halves
        first, second = head, prev
        while second:
            # Save next pointers
            tmp1, tmp2 = first.next, second.next
            
            # Re-assign pointers
            first.next = second
            second.next = tmp1
            
            # Move pointers forward
            first, second = tmp1, tmp2
