# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # initialization for previous node, set to -infinity as dummy value
        prev_node = ListNode(float('-inf'))
        # initialization for new linked list
        dummy_head = ListNode(float('-inf'))
        last_distinct_node = None
        cur = dummy_head
        
        while head:
            if head.val != prev_node.val and (head.next and head.val != head.next.val or not head.next):
                # add distinct node to new linked list
                cur.next = head
                cur = cur.next
                # update last distinct node
                last_distinct_node = head
            # update previous node and head node position                
            prev_node, head = head, head.next
        if last_distinct_node:
            # remove unnecessary tail part after last distinct node
            last_distinct_node.next = None
        
        # return head of new linked list
        return dummy_head.next