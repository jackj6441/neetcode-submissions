# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a = []
        tmp = head
        while tmp:
            a.append(tmp)
            tmp = tmp.next
        if len(a) == n:
            return head.next
        remove = a[len(a)-n]
        t = a[len(a)-n-1]
        t.next = remove.next
        print(t.val)
        return head

