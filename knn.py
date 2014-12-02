# vim:filetype=python:fileencoding=utf-8

import math, operator


class KNNSolver(object):
    """ Solver for the k-Nearest Neighbors Problem """

    def __init__(self, points):
        self.points = points

    def closest_to(self, point, k=1):
        nearest = dict()

        for p in self.points:
            if (p == point): continue
            dist = self._dist(p, point)
            nearest.setdefault(p, dist)

        # TODO: get rid of this sort and subsequent list traversal by
        # perhaps using a list of length `k` or other data structure
        # that keeps O(n) complexity by prioritizing the cloest as it
        # iterates through `points`
        sorted_points = sorted(nearest.items(), key=operator.itemgetter(1))

        return [p for p, dist in sorted_points][0:k]

    def _dist(self, a, b):
        """ Basic Euclidean distance between a and b. """
        # TODO: expand beyond 2D space
        x1, x2 = a[0], b[0]
        y1, y2 = a[1], b[1]
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
