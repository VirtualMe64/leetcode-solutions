# Problem: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list
# Runtime: 125 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        if n == 1: return None

        curr = head
        for _ in range((n // 2) - 1):
            curr = curr.next
        curr.next = curr.next.next

        return head