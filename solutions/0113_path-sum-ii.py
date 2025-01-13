# Problem: https://leetcode.com/problems/path-sum-ii
# Runtime: 29 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        if root.left == None and root.right == None:
            if targetSum - root.val == 0:
                return [[root.val]]

        res1 = self.pathSum(root.left, targetSum - root.val)
        res2 = self.pathSum(root.right, targetSum - root.val)
        
        return [[root.val] + x for x in res1 + res2]