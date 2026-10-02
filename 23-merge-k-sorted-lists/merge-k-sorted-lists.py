# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        curr.next = l1 or l2

        return dummy.next

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        return self.merge(lists, 0, len(lists)-1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]

        mid = (left + right)//2

        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)

        return self.mergeTwoLists(l1, l2)