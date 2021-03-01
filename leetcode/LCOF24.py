# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        p_previous = None
        p_current = head
        p_next = None

        while p_current:
            p_next = p_current.next
            if p_next is None:
                new_head = p_current
            p_current.next = p_previous
            p_previous = p_current
            p_current = p_next
        
        return new_head