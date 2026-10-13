# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head:
            return head

        l, tail = 1, head

        while tail.next:
            tail = tail.next
            l += 1

        k = k%l
        if k == 0:
            return head

        curr = head
        for i in range(l - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        tail.next = head

        return new_head