""" This problem is so famous and I had heard about to quite often so I decided to solve it.
They key is to declare two special variables - curr and prev.
curr keep track of the current node (obviously as the name suggests).
prev keeps track of the prev as as the forward connections are broken
and backward connections are made.
For example:
OK so imagine we have this list: 
1->2->3->4->5->NULL
after the first iteration through the main loop, the above list should look like this:
NULL<-1 2->3->4->5->NULL
by doing, this, we've essentially lost all information between nodes 1 and 2. but we don't want
to do that do we? which is why the variable prev is so important.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # print(head)
        if head is None or head.next is None:
            return head
        curr = head
        prev = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev