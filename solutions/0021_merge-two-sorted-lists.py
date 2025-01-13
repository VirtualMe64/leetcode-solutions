# Problem: https://leetcode.com/problems/merge-two-sorted-lists
# Runtime: 16 ms

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        vals = []
        while list1 != None and list2 != None:
            v1 = list1.val
            v2 = list2.val
            if v1 < v2:
                vals.append(v1)
                list1 = list1.next
            else:
                vals.append(v2)
                list2 = list2.next

        while list1 != None:
            vals.append(list1.val)
            list1 = list1.next
        while list2 != None:
            vals.append(list2.val)
            list2 = list2.next
        out = None
        last = None
        for val in vals:
            newNode = ListNode(val)
            if last == None:
                last = newNode
                out = last
            else:
                last.next = newNode
                last = newNode
        return out