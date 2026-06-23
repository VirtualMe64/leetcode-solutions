# Problem: https://leetcode.com/problems/rotate-list
# Runtime: 0 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head

        listLen = 0
        curr = head
        while True:
            if curr is None:
                break
            
            curr = curr.next
            listLen += 1

        realK = -k % listLen
        curr = head
        out = None
        currOut = None
        for i in range(realK + listLen):
            if i == realK:
                out = ListNode(curr.val)
                currOut = out
            elif i > realK:
                currOut.next = ListNode(curr.val)
                currOut = currOut.next
    
            if curr.next is None:
                curr = head
            else:
                curr = curr.next
    
        
        return out