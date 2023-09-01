# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
#         cur = head
#         greater_list = ListNode(0)
#         smaller_list = ListNode(0)

#         while cur:
#             if cur.val < x:
#                 smaller_list.next = cur
#                 cur = cur.next
#             else:
#                 greater_list.next = cur
#                 cur = cur.next
        
#         smaller_list_head = smaller_list.next
#         greater_list_head = greater_list.next

#         cur_small = smaller_list_head
#         # temp = cur_small

#         while cur_small.next is not None:
#             if cur_small:
#                 cur_small = cur_small.next
#         cur_small.next = greater_list_head

#         return smaller_list_head
              

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur = head
        greater_list = ListNode(0)
        smaller_list = ListNode(0)
        greater_head = greater_list
        smaller_head = smaller_list

        while cur:
            if cur.val < x:
                smaller_list.next = cur
                smaller_list = smaller_list.next
            else:
                greater_list.next = cur
                greater_list = greater_list.next
            cur = cur.next
        
        smaller_list.next = greater_head.next 
        greater_list.next = None
        
        return smaller_head.next

