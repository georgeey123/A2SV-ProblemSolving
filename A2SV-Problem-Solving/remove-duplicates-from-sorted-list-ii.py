# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        tail = dummy

        while cur and cur.next:
            if cur.val != cur.next.val:
                tail = cur
                cur = cur.next
            else:
                while cur and tail.next.val == cur.val:
                    cur = cur.next
                tail.next = cur

        return dummy.next
