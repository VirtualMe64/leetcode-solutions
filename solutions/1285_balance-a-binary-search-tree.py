# Problem: https://leetcode.com/problems/balance-a-binary-search-tree
# Runtime: 25 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []

        def dfs(root):
            if root.left: dfs(root.left)
            values.append(root.val)
            if root.right: dfs(root.right)

        dfs(root)
        # values now contains the values of the tree sorted

        def buildTree(values):
            if len(values) == 0:
                return None
            if len(values) == 1:
                return TreeNode(values[0])
            
            middle = len(values) // 2
            leftTree = buildTree(values[:middle])
            rightTree = buildTree(values[middle + 1:])
            return TreeNode(values[middle], leftTree, rightTree)
        
        return buildTree(values)