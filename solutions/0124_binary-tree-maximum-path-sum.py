# Problem: https://leetcode.com/problems/binary-tree-maximum-path-sum
# Runtime: 162 ms

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # idea: dynamic programming where on longest path ending at node, not including higher nodes
        stack = []
        queue = [root]
        while len(queue) > 0: # todo: make more efficient
            curr = queue.pop(0)
            stack.insert(0, curr)
            if curr.left != None:
                queue.append(curr.left)
            if curr.right != None:
                queue.append(curr.right)
                
        resDict = {}
        currBest = None
        for node in stack:
            val = node.val
            left = resDict[node.left] if node.left != None else 0
            right = resDict[node.right] if node.right != None else 0
            bestEnding = max(val, val + right, val + left)
            resDict[node] = bestEnding

            best = max(bestEnding, val + left + right)
            if currBest == None or best > currBest:
                currBest = best

        return currBest