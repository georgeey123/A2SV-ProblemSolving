# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        # Initialize pointers for reversing the linked list.
        prev = None
        cur = head
        next_node = head.next

        # Reverse group
        while cur:
            cur.next = prev
            prev = cur
            cur = next_node
            if next_node:
                next_node = next_node.next

        # Return the new head and the tail of the reversed sublist.
        return prev, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Initialize the starting pointer.
        starting_head = head
        # Initialize the pointer for connecting the previous tail to the new head.
        first_node = None

        while starting_head:
            val = k
            second_node = starting_head
            while val > 1:
                second_node = second_node.next
                 # If there are fewer than 'k' nodes left, return the original head.
                if not second_node:
                    return head
                val -= 1

             # Store the node after the 'k'-group.
            temp = second_node.next 
            # Disconnect the 'k'-group from the rest of the list.
            second_node.next = None  

            # Reverse the 'k'-group and get its new head and tail.
            headd, tail = self.reverse(starting_head)

            if first_node:
                # If it's not the first 'k'-group, connect the previous tail to the new head.
                first_node.next = headd
            else:
                # If it's the first 'k'-group, update the head of the entire list.
                head = headd  

            # Connect the tail of the reversed 'k'-group to the node after it.
            tail.next = temp 
            # Update the 'first_node' to the new tail of the reversed 'k'-group. 
            first_node = tail  
             # Move 'starting_head' to the node after the reversed 'k'-group.
            starting_head = temp 

        return head





                 

