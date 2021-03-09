# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, lists, lo, hi):
        if lo == hi:
            return lists[lo]
        if lo > hi:
            return None
        mid = (lo + hi) >> 1
        return self.merge_two(
            self.merge(lists, lo, mid),
            self.merge(lists, mid + 1, hi)
        )
    
    def merge_two(self, l1, l2):
        merge_head = None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            merge_head = l1
            merge_head.next = self.merge_two(l1.next, l2)
        else:
            merge_head = l2
            merge_head.next = self.merge_two(l1, l2.next)
        return merge_head
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.merge(lists, 0, len(lists) - 1)
