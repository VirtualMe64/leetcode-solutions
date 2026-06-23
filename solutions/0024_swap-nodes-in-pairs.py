# Problem: https://leetcode.com/problems/swap-nodes-in-pairs
# Runtime: 40 ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last2 = []
        curr = head
        ret = head
        
        index = 0
        while curr != None:
            nextNode = curr.next
            if index % 2 == 1:
                last2[-1].next = nextNode
                curr.next = last2[-1]
                if len(last2) > 1:
                    last2[-2].next = curr
                if index == 1:
                    ret = curr
                last2.append(last2[-1])
            else:
                last2.append(curr)
            if len(last2) > 2:
                last2.pop(0)
            curr = nextNode
            index += 1

        return ret