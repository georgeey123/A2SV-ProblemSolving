# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        left = dummy_node
        right = head

        # shift right n times 
        while n > 0 and right:
            right = right.next
            n -= 1

        # shift left and right
        while right:
            left = left.next
            right = right.next

        # delete node
        left.next = left.next.next

        return dummy_node.next
