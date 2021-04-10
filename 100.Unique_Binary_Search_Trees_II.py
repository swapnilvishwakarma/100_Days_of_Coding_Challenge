# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> list:
        def generate(l, r):   # split between [l, r)
            if l == r:
                return [None]
            nodes = []
            for i in range(l, r):
                for lchild in generate(l, i):
                    for rchild in generate(i+1, r):
                        node = TreeNode(i+1)   # +1 to convert the index to the actual value
                        node.left = lchild
                        node.right = rchild
                        nodes.append(node)
            return nodes
        return generate(0, n) if n else []