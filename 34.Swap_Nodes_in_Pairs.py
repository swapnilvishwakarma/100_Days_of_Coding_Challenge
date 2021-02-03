# Given a linked list, swap every two adjacent nodes and return its head.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head:                                           # first (head) node exists
            h = head.next                                  # second node
            if h:                                          # second node exists => a pair exists
                h.next, head.next = head, h.next           # swap node pair, first node with second => 'h' is new head
                h.next.next = self.swapPairs(h.next.next)  # recurse on next pair head
                return h                                   # returns the new head of a swapped node pair
        return head                                        # returns when a node pair doesn't exist
