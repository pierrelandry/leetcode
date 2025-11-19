# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            div =total % 10

            current.next = ListNode(div)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next


if __name__ == '__main__':
    s = Solution()

    # Helper function to create linked list from array
    def create_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper function to convert linked list to array
    def to_array(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    # Example 1: l1 = [2,4,3], l2 = [5,6,4] -> [7,0,8]
    l1 = create_list([2, 4, 3])
    l2 = create_list([5, 6, 4])
    result = s.addTwoNumbers(l1, l2)
    print(f"Example 1: {to_array(result)}")  # Expected: [7, 0, 8]

    # Example 2: l1 = [0], l2 = [0] -> [0]
    l1 = create_list([0])
    l2 = create_list([0])
    result = s.addTwoNumbers(l1, l2)
    print(f"Example 2: {to_array(result)}")  # Expected: [0]

    # Example 3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] -> [8,9,9,9,0,0,0,1]
    l1 = create_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_list([9, 9, 9, 9])
    result = s.addTwoNumbers(l1, l2)
    print(f"Example 3: {to_array(result)}")  # Expected: [8, 9, 9, 9, 0, 0, 0, 1]
