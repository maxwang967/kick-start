# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for i in range(n):
            if fast is not None:
                fast = fast.next
        if fast is None:
            return head.next
        while fast is not None and fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head