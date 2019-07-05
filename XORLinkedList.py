# An XOR linked list is a more memory efficient doubly linked list. 
# Instead of each node holding next and prev fields, it holds a field named both, 
# which is an XOR of the next node and the previous node. Implement an XOR linked list;
# it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

# If using a language that has no pointers (such as Python), you can assume you have access to get_pointer
# and dereference_pointer functions that converts between nodes and memory addresses.

# Using _ctypes for "memory addressing, pointers"
import _ctypes

def XOR(a, b = None):
    return bool(a) ^ bool(b)

class XOR_List():
    def __init__(self):
        self.startNode = None
        self.size = 0
    
    def add(self, elem):
        if self.startNode is None:
            self.startNode = Node(elem)
        else:
            # 1. get last index
            # 2. insert Node(elem)
            pass
        self.size += 1
    
    def get(self, index):
        if index > self.size:
            raise ValueError("Index out of bounds!")
        i = 0
        node_ptr = ptr(self.startNode)
        while node_ptr > 0:
            # get node at "index = i"
            node = deref_ptr(node_ptr)
            # if this is the right index, return node
            if(i == index):
                return node
            # set pointer to next node
            node_ptr = node.getNext 
            i += 1

class Node():
        # If first in list, there will be no previous node
        def __init__(self, obj, prev = None):
            self.obj = obj
            self.both = XOR(ptr(prev))

        def setBoth(self, prev, next):
            self.both = XOR(ptr(prev), ptr(next))

        # Returns pointer to next node
        def getNext(self):
            # if next exists, return ptr
            # else, return None
            pass
    
# Returns pointer of object
def ptr(obj):
    return id(obj)

# Returns the object, located at pointer
def deref_ptr(ptr):
    return _ctypes.PyObj_FromPtr(ptr)

val = 22

print(deref_ptr(id(val)))