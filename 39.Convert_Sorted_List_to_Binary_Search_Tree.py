# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
            
        return self.constructBST(arr, 0, len(arr)-1)
    
    def constructBST(self, arr, left, right):
        if left > right:
            return None
        
        mid = math.floor(left + (right - left)/2)
        root = TreeNode(arr[mid])
        
        root.left = self.constructBST(arr, left, mid-1)
        root.right = self.constructBST(arr, mid + 1, right)
        
        return root