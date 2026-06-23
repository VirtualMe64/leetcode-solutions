# Problem: https://leetcode.com/problems/reverse-nodes-in-k-group
# Runtime: 3 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # step 1: get length of list
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        out = None
        newGroupStart = None
        oldGroupStart = None
        ptr1 = head
        ptr2 = head.next
        for group in range(n // k):
            # at start: ptr1 is first in group and ptr2 is second in group
            newGroupStart = ptr1

            for i in range(k - 1):
                temp = ptr2.next
                ptr2.next = ptr1
                ptr1 = ptr2
                ptr2 = temp

            if out is None:
                out = ptr1

            if oldGroupStart is not None:
                oldGroupStart.next = ptr1

            oldGroupStart = newGroupStart

            ptr1 = ptr2
            if ptr2: ptr2 = ptr2.next

        oldGroupStart.next = ptr1

        return out