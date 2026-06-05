# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = 0,0
        
        dummy = ListNode()
        node = dummy
        pas = 0
        while l1 or l2 or pas:
            cur = 0
            if l1: 
                cur += l1.val
                l1 = l1.next
            if l2: 
                cur += l2.val
                l2 = l2.next
            if pas: cur += 1
            pas = 0
            if cur >= 10:
                pas = 1
                cur -= 10
            node.next = ListNode(cur)
            node = node.next
        # if pas:
            
        # if l1:
        #     node.next = l1
        # elif l2:
        #     node.next = l2
        # elif pas:
        #     node.next = ListNode(1)
        return dummy.next

