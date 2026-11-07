class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        # left : give least recent used , right : give most recent used 
        # initially these are empty nodes and we are going to insert nodes in between them so the LRU node will always be self.left.next
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        A, B = node.prev, node.next
        A.next = B
        B.prev = A

    def insert(self, node):
        A , B = self.right.prev, self.right
        A.next = B.prev = node
        node.prev, node.next = A, B

    def get(self, key: int) -> int:
        if key in self.cache:
            temp = self.cache[key].val
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return temp
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    
    # this is the brute force which gets time limit exceeds hence use hashmap and Double linked list
    # def __init__(self, capacity: int):
    #     self.cache = [] 
    #     self.capacity = capacity 

    # def get(self, key: int) -> int:
    #     for i in range(len(self.cache)):
    #         if self.cache[i][0] == key:
    #             temp = self.cache.pop(i)
    #             self.cache.append(temp)
    #             return temp[1]
    #     return -1
        
    # def put(self, key: int, value: int) -> None:
    #     for i in range(len(self.cache)):
    #         if self.cache[i][0] == key:
    #             temp = self.cache.pop(i)
    #             temp[1] = value
    #             self.cache.append(temp)
    #             return

    #     if self.capacity == len(self.cache):
    #         self.cache.pop(0)

    #     self.cache.append([key,value])


