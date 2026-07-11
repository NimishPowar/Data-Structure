# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
        for i in range(0,count // 2):
            head = head.next
        return head
        