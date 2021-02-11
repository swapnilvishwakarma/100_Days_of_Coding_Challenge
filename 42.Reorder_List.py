# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None
        dummy = head
        l = []
        while dummy != None:
            l.append(dummy)
            dummy = dummy.next
            
        mid = len(l)//2
        for i in range(mid):
            l[i].next = l[-(i+1)]
            l[-(i+1)].next = l[(i+1)]
        
        l[mid].next = None
        return head    