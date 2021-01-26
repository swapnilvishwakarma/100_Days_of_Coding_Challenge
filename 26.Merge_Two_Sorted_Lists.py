# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing 
# together the nodes of the first two lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode(0) 
        ptr = dummy
        
        while True: 
            if l1 is None: 
                ptr.next = l2 
                break
            if l2 is None: 
                ptr.next = l1
                break
            if l1.val <= l2.val: 
                ptr.next = l1 
                l1 = l1.next
            else: 
                ptr.next = l2 
                l2 = l2.next
            ptr = ptr.next

        return dummy.next


sol = Solution()
print(sol.mergeTwoLists([1,2,4], [1,3,4]))
