#!/usr/bin/env python3
"""
Classic Google PageRank algorithm with explicit number of iterations.
See https://en.wikipedia.org/wiki/PageRank#Python.

Returns
-------
ranking of nodes (pages) in the adjacency matrix
"""

import numpy as np

def pagerank(M, num_iterations: int = 100, d: float = 0.85):
    """PageRank: The trillion dollar algorithm.

    Parameters
    ----------
    M : numpy array
        adjacency matrix where M_i,j represents the link from 'j' to 'i', such that for all 'j'
        sum(i, M_i,j) = 1
    num_iterations : int, optional
        number of iterations, by default 100
    d : float, optional
        damping factor, by default 0.85

    Returns
    -------
    numpy array
        a vector of ranks such that v_i is the i-th rank from [0, 1],
        v sums to 1

    >>> M = np.array([[0, 0, 0, 0, 1],
    ...     [0.5, 0, 0, 0, 0],
    ...     [0.5, 0, 0, 0, 0],
    ...     [0, 1, 0.5, 0, 0],
    ...     [0, 0, 0.5, 1, 0]])
    >>> v = pagerank(M, 100, 0.85)
    >>> v
    array([[0.25419178],
           [0.13803151],
           [0.13803151],
           [0.20599017],
           [0.26375504]])
    >>> total = 0
    >>> for col in v:
    ...     total += col[0]
    >>> round(total) == 1.0
    True
    """
    N = M.shape[1]
    v = np.random.rand(N, 1)
    v = v / np.linalg.norm(v, 1)
    M_hat = (d * M + (1 - d) / N)
    for i in range(num_iterations):
        v = M_hat @ v
    return v

if __name__ == "__main__":
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])
