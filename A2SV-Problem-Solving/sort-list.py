# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(list1, list2):
            part1 = list1
            part2 = list2

            dummy = ListNode(0)
            curr = dummy
            while part1 and part2:
                if part1.val <= part2.val:
                    curr.next = part1
                    part1 = part1.next
                    curr = curr.next

                else:
                    curr.next = part2
                    part2 = part2.next
                    curr = curr.next

            if part1:
                curr.next = part1
            elif part2:
                curr.next = part2

            return dummy.next

        def sort(head):
            if not head or not head.next:
                return head
            
            slow = fast = prev = head
            while fast:
                prev = slow
                slow = slow.next
                fast = fast.next
                if fast:
                    fast = fast.next
            prev.next = None
            
            list1 = sort(head)
            list2 = sort(slow)
            return merge(list1, list2)

        ans = sort(head)
        return ans
