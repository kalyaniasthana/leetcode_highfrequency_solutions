"""
very similar to ADD STRINGS and ADD BINARY. 
only difference is that we have to use linked lists instead of array.
be careful about when you're creating the new list node. 
this problem is easy with a compiler but not on a google doc/whiteboard interview
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0, None)
        temp_head = l3
        carry = 0
        while l1 is not None or l2 is not None:
            sum_ = carry
            if l1 is not None:
                sum_ += l1.val
                l1 = l1.next
            if l2 is not None:
                sum_ += l2.val
                l2 = l2.next
            l3.val = sum_%10
            carry = sum_//10
            if l1 is not None or l2 is not None:
                l3.next = ListNode(0, None)
                l3 = l3.next      
        if carry != 0:
            l3.next = ListNode(0, None)
            l3 = l3.next
            l3.val = carry
        return temp_head