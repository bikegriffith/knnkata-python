[ ![Codeship Status for bikegriffith/knnkata-python](https://codeship.com/projects/a67f82f0-cfdc-0132-73af-7637bc41f5cd/status?branch=master)](https://codeship.com/projects/76823)

knnkata-python
==============

Implementation of a python solution to the k Nearest Neighbors problem

Given a set of input points as `(x, y)` tuples, for example:

    solver = KNNSolver([                                                        
            (1, 2),                                                            
            (1, 1),                                                            
            (1, 4),                                                            
            (2, 3),                                                            
            ...                                                            
            (6, 7),                                                            
            (8, 1),                                                            
            (8, 9),                                                            
        ])

the solver is able to find the geometrically closest neighbors, for some requested number of neighbors, "k".

    >>> input_point = (1, 2)
    >>> two_closest_points = solver.closest_to(input_point, 2)
    >>> print two_closest_points
    [(1, 1), (2, 3)]

The algorithm I'm using here in the first pass of this exercise is naive.  It first iterates over all "points" - O(N) - and then sorts them - O(NlogN) - before grabbing the first k values off the head of the sorted list.  See TODOs for some thoughts on how to improve (and TODO for adding support for higher dimensional inputs)

Running Tests
-------------

    pip install nose
    nosetests
