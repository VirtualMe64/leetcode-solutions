# Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list
# Runtime: 0 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr != None:
            length += 1
            curr = curr.next
        
        removeAfter = length - n

        if removeAfter == 0:
            return head.next
        
        curr = head
        for _ in range(removeAfter - 1):
            curr = curr.next
        curr.next = curr.next.next

        return head