# Q2 Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = ListNode(0)
        curr = head
        carry = 0
        while l1 or l2 or carry == 1:
            num = carry + (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0)
            carry = 1 if num > 9 else 0
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            curr.next = ListNode(num % 10)
            curr = curr.next
        return head.next