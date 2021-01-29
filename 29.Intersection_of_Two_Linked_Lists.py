# Write a program to find the node at which the intersection of two singly linked lists begins.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        return self.withConstantSpaceAndLinearTime(headA, headB)
      
    def getLength(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length
    
    def withConstantSpaceAndLinearTime(self, headA, headB):
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        if lenB > lenA:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA
        
        diff = lenA - lenB
        while diff:
            headA = headA.next
            diff -= 1
        
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        return headA