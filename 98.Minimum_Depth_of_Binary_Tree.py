# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # BFS Approach
        if not root:
            return 0
        
        q = collections.deque()
        q.append((root, 1))
        
        while q:
            node, depth = q.popleft()
            
            if not node.left and not node.right:
                return depth
            
            if node.left:
                q.append((node.left, depth + 1))
                
            if node.right:
                q.append((node.right, depth + 1))
        

        # DFS Approach
#         if not root:
#             return 0
        
#         if not root.left and not root.right:
#             return 1
        
#         if not root.left and root.right:
#             return 1 + self.minDepth(root.right)
        
#         if not root.right and root.left:
#             return 1 + self.minDepth(root.left)
        
#         return 1 + min(self.minDepth(root.right), self.minDepth(root.left))