# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        cur_postion = 1
        p_cur = head
        p_pre = None
        p_next = None
        p_fore = None
        p_left = None
        p_right = None
        new_head = None
        while p_cur:
            # print(p_cur.val)
            p_next = p_cur.next
            if cur_postion >= left and cur_postion < right:
                if cur_postion == left:
                    p_fore = p_pre
                    p_left = p_cur
                    p_cur.next = None
                else:
                    p_cur.next = p_pre                
            if cur_postion == right:
                p_cur.next = p_pre
                p_right = p_cur
                if p_fore:
                    p_fore.next = p_right
                else:
                    new_head = p_right
                if p_next:
                    p_left.next = p_next
                break
            cur_postion += 1
            p_pre = p_cur
            p_cur = p_next
        if new_head:
            return new_head
        else:
            return head