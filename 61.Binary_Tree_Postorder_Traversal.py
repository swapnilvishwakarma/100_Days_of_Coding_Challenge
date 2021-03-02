# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        
        while True:
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.right  
            
            if not stack:
                return res[: : -1]
            node = stack.pop()
            root = node.left   

        return res[: : -1]