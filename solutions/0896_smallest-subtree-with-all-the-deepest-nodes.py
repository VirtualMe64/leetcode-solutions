# Problem: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes
# Runtime: 0 ms

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # step 1: find depth, store deepest
        max_depth = 0
        deepest_nodes = []
        parent = {}

        # use dfs to find depth
        queue = deque()
        queue.append((root, 0))
        while len(queue) > 0:
            node, depth = queue.popleft()

            if depth > max_depth:
                max_depth = depth
                deepest_nodes.clear()
            if depth == max_depth:
                deepest_nodes.append(node)

            if node.left:
                queue.append((node.left, depth + 1))
                parent[node.left] = node
            if node.right:
                queue.append((node.right, depth + 1))
                parent[node.right] = node

        if len(deepest_nodes) == 1:
            return deepest_nodes[0]

        # step 2: work backwards from first deepest node until all are included
        rem = set(deepest_nodes[1:])

        prev = deepest_nodes[0]
        curr = parent[deepest_nodes[0]]
        
        while curr != root:
            if curr.left and curr.left != prev:
                start = curr.left
            elif curr.right and curr.right != prev:
                start = curr.right
            else:
                prev = curr
                curr = parent[curr]
                continue
            
            queue = deque()
            queue.append(start)
            while len(queue) > 0:
                node = queue.popleft()
                if node in rem:
                    rem.remove(node)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)


            if len(rem) == 0:
                return curr
            
            prev = curr
            curr = parent[curr]


        return root