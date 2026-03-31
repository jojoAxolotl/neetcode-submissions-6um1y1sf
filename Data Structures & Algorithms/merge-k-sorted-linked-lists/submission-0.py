# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()

        min_heap = []
        for i, node in enumerate(lists): # T: O(k*logk)
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        cur = res
        while min_heap: # T: O(N*logk)
            val, i, node = heapq.heappop(min_heap) # curr_min_node
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return res.next

# T: O(N*logk) k: len(lists) N: amount of all nodes
# S: O(k) Heap的大小：任何時間點，min_heap 裡最多只會存放 k 個元素（每個 List 貢獻一個）。

