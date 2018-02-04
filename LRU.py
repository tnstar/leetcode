class Node(object):
    def __init__(self,key, val):
        self.next = None
        self.prev = None
        self.val = val
        self.key = key

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.node_map = {}
        self.link_head = Node(-1,-1)
        self.link_tail = Node(-1,-1)
        self.link_head.next = self.link_tail
        self.link_tail.prev = self.link_head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.node_map:
            val = self.node_map[key].val
            prev_node = self.node_map[key].prev
            next_node = self.node_map[key].next
            # remove from double linked list
            prev_node.next = next_node
            next_node.prev = prev_node
            # append after linkhead
            next_node = self.link_head.next
            self.link_head.next = self.node_map[key]
            self.node_map[key].prev = self.link_head
            self.node_map[key].next = next_node
            next_node.prev = self.node_map[key]
            return val
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # if it is already in the node map, just get the item and change it's val
        if key in self.node_map:
            self.get(key)
            self.node_map[key].val = value
        else:
            # this is a new key we need to:
            # 1. append to head if size allow
            # 2. delete what's in tail and append this guy to front
            if len(self.node_map)>=self.cap:
                tail_node = self.link_tail.prev
                tail_node.prev.next = self.link_tail
                self.link_tail.prev = tail_node.prev
                del self.node_map[tail_node.key]
                del tail_node
            new_node = Node(key, value)
            self.node_map[key] = new_node
            next_node = self.link_head.next
            self.link_head.next = new_node
            new_node.prev = self.link_head
            new_node.next = next_node
            next_node.prev = new_node
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# Test1
# lru = LRUCache(1)
# lru.put(2,1)
# lru.get(2)
# lru.put(3,2)
# lru.get(2)
# lru.get(3)
# Test2
lru = LRUCache(2)
lru.put(1,1)
lru.put(2,2)
lru.get(1)
lru.put(3,3)
lru.get(2)
lru.put(4,4)
lru.get(1)
lru.get(3)
lru.get(4)