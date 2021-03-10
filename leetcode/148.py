# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        # print(f"{head}-{mid}")
        left = self.sortList(head)
        right = self.sortList(mid)
        result = dummy = ListNode(0)
        while left is not None and right is not None:
            if left.val < right.val:
                dummy.next = left
                left = left.next
            else:
                dummy.next = right
                right = right.next
            dummy = dummy.next
        dummy.next = left if left is not None else right
        return result.next