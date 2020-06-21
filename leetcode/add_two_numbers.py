from os.path import join
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        numbers = []
        carry = 0
        while True:
            if l1 is not None and l2 is not None:
                number1 = l1.val
                number2 = l2.val
                add_sum = number1 + number2 + carry
                numbers.append(add_sum % 10)
                if add_sum >= 10:
                    carry = 1
                else:
                    carry = 0
                l1 = l1.next
                l2 = l2.next
            elif l1 is None and l2 is not None:
                number1 = 0
                number2 = l2.val
                add_sum = number1 + number2 + carry
                if add_sum >= 10:
                    numbers.append(add_sum % 10)
                    if l2.next is None:
                        numbers.append(1)
                        return self.generateListNode(numbers)
                    else:
                        carry = 1
                else:
                    if l2.next is None:
                        numbers.append(add_sum)
                        return self.generateListNode(numbers)
                    else:
                        numbers.append(add_sum % 10)
                        carry = 0
                l2 = l2.next
            elif l1 is not None and l2 is None:
                number1 = l1.val
                number2 = 0
                add_sum = number1 + number2 + carry
                
                if add_sum >= 10:
                    numbers.append(add_sum % 10)
                    if l1.next is None:
                        numbers.append(1)
                        return self.generateListNode(numbers)
                    else:
                        carry = 1
                else:
                    if l1.next is None:
                        numbers.append(add_sum)
                        return self.generateListNode(numbers)
                    else:
                        numbers.append(add_sum % 10)
                        carry = 0
                l1 = l1.next
            elif l1 is None and l2 is None:
                if carry == 1:
                    numbers.append(1)
                return self.generateListNode(numbers)

    def generateListNode(self, numnbers: List[int]):
        head = ListNode(numnbers[0])
        old_node = head
        for i in range(1, len(numnbers)):
            new_node = ListNode(numnbers[i])
            old_node.next = new_node
            old_node = new_node
        return head


if __name__ == "__main__":
    solution = Solution()
    test_node1 = solution.generateListNode([9, 1, 6])
    test_node2 = solution.generateListNode([0])
    result = solution.addTwoNumbers(test_node1, test_node2)
    print(result)
