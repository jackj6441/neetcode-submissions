# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        node = dummy
        l, r = head, head
        m = {}
        while r.next:
            m[r.next] = r
            r = r.next
        while l != r and l.next != r:
            nextl = l.next
            prevr = m[r]

            node.next = l
            node = node.next

            node.next = r
            node = node.next

            l = nextl
            r = prevr

            node.next = None

        if l == r:
            node.next = l
            node = node.next
            node.next = None
        elif l.next == r:
            node.next = l
            node = node.next
            node.next = r
            node = node.next
            node.next = None
