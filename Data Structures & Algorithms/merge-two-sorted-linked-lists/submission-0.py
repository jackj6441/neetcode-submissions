# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = list1, list2
        dump = ListNode()
        tmp = dump
        while c1 != None and c2 != None:
            if c1.val > c2.val:
                tmp.next = c2
                c2 = c2.next
            else:
                tmp.next = c1
                c1 = c1.next
            tmp = tmp.next
        if c1 != None:
            tmp.next = c1
        else:
            tmp.next = c2
        return dump.next
            