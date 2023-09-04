# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_list = ListNode(0)
        odd_list = ListNode(0)
        odd_head = odd_list
        even_head = even_list

        cur = head
        count = 1

        while cur:
            if count % 2 == 0:
                even_list.next = cur
                even_list = even_list.next
            else:
                odd_list.next = cur
                odd_list = odd_list.next
            cur = cur.next
            count += 1

        odd_list.next = even_head.next
        even_list.next = None

        return odd_head.next
