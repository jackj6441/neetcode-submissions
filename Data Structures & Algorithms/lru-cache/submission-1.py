class ListNode:
    def __init__(self, value=0,key = 0, next = None,prev = None):
        self.value = value
        self.next = next
        self.prev = prev
        self.key = key
class LRUCache:

    def __init__(self, capacity: int):
        self.limit = capacity

        self.m = {}
        self.left = ListNode()
        self.right = ListNode()

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1

        node = self.m[key]

        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            old_node = self.m[key]
            self.remove(old_node)

        node = ListNode(value, key)
        self.m[key] = node
        self.insert(node)

        if len(self.m) > self.limit:
            lru = self.left.next
            self.remove(lru)
            del self.m[lru.key]
        

        
