# Problem: https://leetcode.com/problems/n-ary-tree-postorder-traversal
# Runtime: 34 ms

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        if len(root.children) == 0:
            return [root.val]
        
        out = []
        for node in root.children:
            out.extend(self.postorder(node))
        out.append(root.val)
        return out