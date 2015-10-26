# 1 -> 3 -> 5
# 2 -> 4
# 3 -> 5
# queue.get()
# queue.empty()
#output is a linked list

from queue import PriorityQueue

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def merge_linked_lists(heads):
    queue = PriorityQueue()
    for head in heads:
        queue.put((head.value, head))
    head = None
    tail = None
    while not queue.empty():
        node = queue.get()[1]
        if node.next:
            node_next = node.next
            queue.put((node_next.value, node_next))
        if not head:
            head = tail = node
        else:
            tail.next = node
            tail = node
    # tie off end. make the tail point to null
    tail.next = None
    return head


# two linked lists  one from a - b, other just c (to null)
a = Node('a')
b = Node('d')
c = Node('c')
a.next = b
d = merge_linked_lists([a,c])
while d:
    print(d.value)
    d = d.next
