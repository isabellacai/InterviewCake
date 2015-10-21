# # finding largest element
# def largest(root_node):
#     if root_node.right:
#         return largest(root_node.right)
#     return root_node.value

# if the rightmost node in the binary search tree
# has a left subtree, then the 2nd largest element (in the overall tree)
# is the rightmost element in the subtree, or if there
# is only a left child, the left child.

def second_largest(root_node):
    if root_node is None:
        return None

    if root_node.left and not root_node.right:
        return largest(root_node.left)

    if root_node.right and not root_node.right.left and not root_node.right.right:
        return root_node.value

    return second_largest(root_node.right)

# It'll take O(h)O(h) time (where hh is the height of the tree) and O(h)O(h) space.
# But that hh space in the call stack ↴ is avoidable. How can we get this down to constant space?


# constant space
def find_second_largest(root_node):
    current = root_node

    while current:
        # case: current is largest and has a left subtree
        # 2nd largest is the largest in that subtree
        if current.left and not current.right:
            return find_largest(current.left)

        # case: current is parent of largest, and
        # largest has no children, so
        # current is 2nd largest
        if current.right and \
           not current.right.left and \
           not current.right.right:
            return current.value

        current = current.right
