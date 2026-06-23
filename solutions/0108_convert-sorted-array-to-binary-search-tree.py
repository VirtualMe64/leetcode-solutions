# Problem: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
# Runtime: 1 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(nums):
            if len(nums) == 0:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            
            middle = len(nums) // 2
            leftTree = buildTree(nums[:middle])
            rightTree = buildTree(nums[middle + 1:])
            return TreeNode(nums[middle], leftTree, rightTree)
        
        return buildTree(nums)