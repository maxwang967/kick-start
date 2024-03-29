# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            tmp = cur.next
            ptr = cur.next
            while tmp and tmp.val == cur.val:
                ptr = tmp.next
                tmp = tmp.next
            cur.next = ptr
            cur = cur.next
        
        return head