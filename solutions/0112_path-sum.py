# Problem: https://leetcode.com/problems/path-sum
# Runtime: 22 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root == None:
            return False

        if root.left == None and root.right == None:
            if targetSum - root.val == 0:
                return True

        res1 = self.hasPathSum(root.left, targetSum - root.val)
        res2 = self.hasPathSum(root.right, targetSum - root.val)
        return res1 or res2 