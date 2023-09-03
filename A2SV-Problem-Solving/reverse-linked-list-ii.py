# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # find range to reverse
        left_prev, cur = dummy, head
        for i in range(left - 1):
            left_prev, cur = cur, cur.next

        #reverse sub-section
        prev = None
        for i in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp

        #update Pointers
        left_prev.next.next = cur
        left_prev.next = prev

        return dummy.next 