# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        targetSum -= root.val
        
        if root.left == None and root.right == None:
            if targetSum == 0:
                return True
            return False
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)