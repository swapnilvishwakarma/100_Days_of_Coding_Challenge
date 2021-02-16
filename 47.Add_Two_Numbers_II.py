# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1 and l2: return l2
        if not l2 and l1: return l1

        result_l1, result_l2 = 0, 0
        while l1 or l2:
            if l1:
                result_l1 = result_l1*10 + l1.val
                l1 = l1.next
            if l2:
                result_l2 = result_l2 * 10 + l2.val
                l2 = l2.next

        result = result_l1 + result_l2

        dummy_head = ListNode(-math.inf)
        curr_node = dummy_head
        for char in str(result):
            curr_node.next = ListNode(int(char))
            curr_node = curr_node.next

        return dummy_head.next