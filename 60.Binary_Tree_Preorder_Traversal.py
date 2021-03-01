# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        result, stack = [], []
        
        while stack or root:
            if root:
                stack.append(root)
                result.append(root.val)
                root = root.left
            
            else:
                node = stack.pop()
                root = node.right

        return result
