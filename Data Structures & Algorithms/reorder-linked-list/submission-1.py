# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        now = slow.next
        prev = slow.next = None
        while now:
            
            tmp = now.next
            now.next = prev
            prev = now
            now = tmp
        head1, head2 = head, prev
        
        while head1 and head2:
            
            tmp1,tmp2 = head1.next,head2.next
            head1.next = head2
            head2.next = tmp1
            
            head2 = tmp2
            head1 = tmp1
            
            

        
