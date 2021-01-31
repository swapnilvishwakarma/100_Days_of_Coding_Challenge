# Reverse a singly linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        next = None
        cur = head
        
        while cur:          # while cur is not None
            next = cur.next  # Saving the n
            cur.next = prev # Reversing the pointer
            prev = cur      # Advance prev to cur
            cur = next       # Advance cur to nxt
            
        return prev
