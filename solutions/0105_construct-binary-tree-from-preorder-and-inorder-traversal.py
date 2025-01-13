# Problem: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
# Runtime: 114 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        center = preorder[0]
        idx = inorder.index(center)
        
        inleft = inorder[0:idx]
        preleft = preorder[1:len(inleft) + 1]
        inright = inorder[idx + 1:]
        preright = preorder[len(inleft) + 1:]

        return TreeNode(center, self.buildTree(preleft, inleft), self.buildTree(preright, inright))