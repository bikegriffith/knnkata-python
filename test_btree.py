# vim:filetype=python:fileencoding=utf-8

import nose.tools as NT
from btree import Node, btree_to_bst


class TestBTreeConversion(object):

    def setup(self):
        """
             5
            / \
           3   9
          /   / \
         1   4*  8*
        """
        self.tree = \
            Node(5,
                Node(3,
                    Node(1, None, None),
                    None
                ),
                Node(9,
                    Node(4, None, None),
                    Node(8, None, None)
                )
            )
        print self.tree

    def test_converts_to_bst_without_changing_shape(self):
        btree_to_bst(self.tree)
        print self.tree
        #assert False
