# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # if there are 1 or 2 nodes no cycle is possible
        if not head or not head.next:
            return None
        
        hare = head
        tortoise = head

        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next

            if hare == tortoise:
                break
        
        if hare == tortoise:
            while head != tortoise:
                tortoise = tortoise.next
                head = head.next
            return head
        else:
            return None


        