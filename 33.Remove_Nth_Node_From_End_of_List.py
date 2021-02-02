# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Follow up: Could you do this in one pass?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        N = 0
        dummy = head
        while dummy:
            N += 1
            dummy = dummy.next
        dummy = head
        step = N - n
        if step == 0:
            head = head.next
        else:
            l = 1
            while l < step:
                dummy = dummy.next
                l += 1
            dummy.next = dummy.next.next
        return head