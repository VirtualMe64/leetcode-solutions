# Problem: https://leetcode.com/problems/add-two-numbers
# Runtime: 46 ms

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        out = ListNode()
        curr = out
        while True:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            res = n1 + n2 + carry
            curr.val = res % 10
            carry = res // 10

            #
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            if (l1 == None and l2 == None):
                if (carry != 0):
                    curr.next = ListNode(carry)
                break
            
            curr.next = ListNode()
            curr = curr.next

        return out