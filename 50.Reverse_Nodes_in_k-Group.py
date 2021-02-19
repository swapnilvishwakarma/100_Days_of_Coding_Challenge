# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# Follow up:
# Could you solve the problem in O(1) extra memory space?
# You may not alter the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseHelper(self, head, k, leftNodes):
        if leftNodes < k:
            return head
    
        count = 0
        prev = None
        current = head
        while current and count < k:
            count += 1
            leftNodes -= 1
            next = current.next
            current.next = prev
            prev = current
            current = next

        if next:
            head.next = self.reverseHelper(next, k, leftNodes)

        return prev
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        leftNodes = 0
        node = head
        while node:
            leftNodes += 1
            node = node.next

        return self.reverseHelper(head, k, leftNodes)