# change the next pointer of each node to point towards the previous node

# 1 -> 2 -> 3
#
# 1 <- 2 <- 3

# 3 -> 2 -> 1

def reverse(head_of_list):
    current = head_of_list
    previous_node = None
    next_node = None

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous
