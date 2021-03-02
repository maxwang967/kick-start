# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        previous = None
        while cur:
            if previous is None:
                previous = cur
                cur = cur.next
                continue
            while cur is not None and previous.val == cur.val:
                cur = cur.next
            previous.next = cur
            previous = cur
        return head