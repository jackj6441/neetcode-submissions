"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        node = dummy
        m = {None:None}
        c = head
        while c:
            m[c] = Node(c.val)
            c = c.next
        c = head
        while c:
            m[c].next = m[c.next]
            m[c].random = m[c.random]
            c = c.next
        return m[head]

        