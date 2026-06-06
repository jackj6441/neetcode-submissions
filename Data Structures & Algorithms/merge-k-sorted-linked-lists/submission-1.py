# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return None
        pq = []
        i = 0
        for l in lists:
            if l != []:
                heapq.heappush(pq, [l.val,i, l])
                i += 1
        i = 0
        dummy = ListNode()
        node = dummy
        while len(pq) > 0:
            cur = heapq.heappop(pq)
            node.next = ListNode(cur[0])
            if cur[2].next:
                l = cur[2].next
                heapq.heappush(pq, [l.val,i, l])
                i += 1
            node = node.next
        return dummy.next

            
