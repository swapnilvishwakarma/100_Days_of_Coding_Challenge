# Given the head of a linked list, rotate the list to the right by k places.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # If no head, return head
        if not head:
            return head
        
        # Make the tail point to the last node while calculating the length of LL
        # Calculate relative position of k as 0 < k < infinity
        # If k is found to have value 0, then return the head as is
        length = 1
        tail = head
        
        while tail.next:
            tail = tail.next
            length += 1
        
        k %= length
        
        if k == 0:
            return head
        
        # New head will always start from length - k
        # Attach tail->next to head and find new head now relative to tail position 
        steps_to_new_head = length - k
        tail.next = head
        
        while steps_to_new_head > 0:
            tail = tail.next
            steps_to_new_head -= 1
        
        # Make new_head point to tail.next
        # And point tail->next to NULL
        new_head = tail.next
        tail.next = None
        
        return new_head