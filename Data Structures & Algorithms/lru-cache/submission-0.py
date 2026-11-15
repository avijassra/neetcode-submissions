class TwoWayLinkedList:
    def __init__(self, key=0, val=None, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = TwoWayLinkedList(-1, -1)
        self.tail = TwoWayLinkedList(-2, -2)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._addToFront(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = TwoWayLinkedList(key, value)
        else:
            node = self.cache[key]
            node.val = value
            self._remove(node)

        self._addToFront(node)
        self.cache[node.key] = node

        if len(self.cache) > self.capacity:
            node = self.tail.prev
            self._remove(node)
            del self.cache[node.key]

    def _remove(self, node: TwoWayLinkedList) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        # del self.cache[node.key]

    def _addToFront(self, node: TwoWayLinkedList) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node