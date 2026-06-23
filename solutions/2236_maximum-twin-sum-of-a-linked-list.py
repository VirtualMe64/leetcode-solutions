# Problem: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list
# Runtime: 49 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []

        while head:
            vals.append(head.val)
            head = head.next
        
        n = len(vals)
        twinSums = [vals[i] + vals[n - i - 1] for i in range(len(vals) // 2)]
        return max(twinSums)