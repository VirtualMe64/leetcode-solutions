# Problem: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array
# Runtime: 751 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        outHead = None
        outTail = None
        curr = head
        nums = set(nums)
        while curr != None:
            if curr.val not in nums:
                if outHead == None:
                    outHead = curr
                else:
                    outTail.next = curr
                outTail = curr
            
            curr = curr.next

        outTail.next = None
        return outHead