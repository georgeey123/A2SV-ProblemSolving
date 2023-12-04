# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, lst in enumerate(lists):
            if lst:
                heappush(heap, (lst.val, i, lst))

        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next

            if node.next:
                heappush(heap, (node.next.val, i, node.next))

        return dummy.next