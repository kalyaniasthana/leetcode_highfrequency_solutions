"""
Super important trick to remember for solving this question: CREATE A NEW HEAD NODE!
Also remember to create a copy of this head node which you will use during 
traversal.
Rest is super easy.
Thank you again to Nick White's Solution Video. I watched only the first 1-2 minutes of his video.
As soon as he said - 'Use a new head node', I knew what to do.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # damnit why are there pointers AAAA
        # create A NEW HEAD NODE 
        # set next node to be the smaller value as we
        # traverse both node lists
        temp_node = ListNode(val=0, next=None)
        curr_node = temp_node
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr_node.next = l1
                curr_node = l1
                l1 = l1.next
            elif l1.val > l2.val:
                curr_node.next = l2
                curr_node = l2
                l2 = l2.next
        while l1 is not None:
            curr_node.next = l1
            curr_node = l1
            l1 = l1.next
        while l2 is not None:
            curr_node.next = l2
            curr_node = l2
            l2 = l2.next
        return temp_node.next