# Given a binary search tree, return a balanced binary search tree with the same node values.
# A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.
# If there is more than one answer, return any of them.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        ns = dfs(root)
        
        def build(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(ns[m])
            root.left, root.right = build(l, m-1), build(m+1, r)
            return root
        
        return build(0, len(ns)-1)