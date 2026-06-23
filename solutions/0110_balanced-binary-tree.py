# Problem: https://leetcode.com/problems/balanced-binary-tree
# Runtime: 7 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        depth = {}
        queue = [root]

        while len(queue) > 0:
            curr = queue[-1]

            if curr.left is None and curr.right is None: # leaf
                depth[id(curr)] = 0
                queue.pop()
                continue

            leftDepth = -1
            leftVisited = True
            if curr.left is not None:
                leftVisited = id(curr.left) in depth
                if leftVisited:
                    leftDepth = depth[id(curr.left)]
                else:
                    queue.append(curr.left)

            rightDepth = -1
            rightVisited = True
            if curr.right is not None:
                rightVisited = id(curr.right) in depth
                if rightVisited:
                    rightDepth = depth[id(curr.right)]
                else:
                    queue.append(curr.right)

            if leftVisited and rightVisited:
                if abs(leftDepth - rightDepth) > 1:
                    return False
                depth[id(curr)] = max(leftDepth, rightDepth) + 1
                queue.pop()
        
        return True