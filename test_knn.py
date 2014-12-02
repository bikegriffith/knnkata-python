# vim:filetype=python:fileencoding=utf-8

import nose.tools as NT
from knn import KNNSolver


class TestKNNSolver(object):

    def setup(self):
        self.points = [
            (1, 2),
            (1, 1),
            (1, 4),
            (2, 3),
            (2, 4),
            (5, 9),
            (5, 8),
            (6, 3),
            (6, 7),
            (8, 1),
            (8, 9),
        ]
        self.solver = KNNSolver(self.points)

    def teardown(self):
        pass

    def test_basic_interface_with_empty_set(self):
        self.solver.points = []
        NT.assert_equals([], self.solver.closest_to(None, 1))

    def test_single_nearest_neighbor(self):
        NT.assert_equals([(1, 2)], self.solver.closest_to((1, 1), 1))

    def test_two_nearest_neighbors(self):
        NT.assert_equals([(1, 1), (2, 3)], self.solver.closest_to((1, 2), 2))
