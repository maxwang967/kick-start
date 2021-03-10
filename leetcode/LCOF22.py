# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        fast = slow = head
        while k > 0:
            if fast is not None:
                fast = fast.next
                k -= 1
        if fast is None:
            return head
        while fast is not None and fast.next is not None:
            fast = fast.next
            slow = slow.next
        return slow.next