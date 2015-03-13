# vim:filetype=python:fileencoding=utf-8


class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node("%s","%s", "%s")' % (self.value, self.left, self.right)


def btree_to_bst(root):
    """
         5
        / \
       3   9
      /   / \
     1   4*  8*
    """

    # O(n^2) but constant memory would be to walk through depth-first and
    # figure out what is supposed to be in "that spot", starting with
    # the left-most and thus smallest
    #
    #
    # O(n log n) is a 3 stepper:
    # 1. convert btree to list
    # 2. sort list
    # 3. copy sorted list back into btree

    def btree_to_list(node, l=None):
        if (l is None):
            l = []
        if (node is None):
            return
        btree_to_list(node.left, l)
        l.append(node.value)
        btree_to_list(node.right, l)
        return l

    def list_to_btree(l, node, i=0):
        if (node is None):
            return
        list_to_btree(l, node.left, i)
        node.value = l.pop(0) #take head of list off, not tail
        list_to_btree(l, node.right, i)
        return root

    l = btree_to_list(root)
    l.sort()
    list_to_btree(l, root)

    return root
