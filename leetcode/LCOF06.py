# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        # 1 stack
        # stack = []
        # result = []
        # while head is not None:
        #     stack.append(head.val)
        #     head = head.next
        # for _ in range(len(stack)):
        #     result.append(stack.pop())
        # return result
        # 2 recusive
        result = []
        def traversal(head):
            if head is not None:
                traversal(head.next)
                result.append(head.val)
        traversal(head)
        return result