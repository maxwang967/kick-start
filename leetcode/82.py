# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur:
            ptr = cur.next
            next_one = None
            while ptr and ptr.next and ptr.val == ptr.next.val:
                next_one = ptr.next
                ptr = ptr.next
            if next_one:
                cur.next = next_one.next
            else:
                cur = cur.next
        
        return dummy.next