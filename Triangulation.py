import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import tri
import networkx as nx
# import numba as nb


# Utility
def crossiterate(L1, L2): return [(a, b) for a in L1 for b in L2 if a != b]
def glue(alofarraylike, L2=None): return np.vstack(alofarraylike) if L2 is None else np.vstack((alofarraylike, L2))
def getRandomPoints(n=100, rangex = 1., rangey = 1.): return point(np.arange(0,n), np.random.uniform([0,0], [rangex, rangey], [n,2]).T)

# Data structure manipulation
def point(keys, pos): return glue(keys,pos)
def triangle(keys, pointkeys): return glue(keys, pointkeys)
def points2seg(keys1, keys2): return glue(keys1, keys2)
def tri2seg(tris): return tris[0], glue(tris[1], tris[2]), glue(tris[1], tris[3]), glue(tris[2], tris[3])
def seg2tri(keys, seg1, seg2, seg3): return triangle(keys, np.array([np.fromiter((x for x in set(p)), int) for p in glue([seg1,seg2,seg3]).reshape(1,6)]).T)

# Graph stuff
def adjMatrix(edgeset): return nx.to_numpy_array(nx.from_edgelist(edgeset))

# For Sorting-based algorithms
def sortPointsK(points): return points[:, points[0].argsort()]
def sortPointsX(points): return points[:, points[1].argsort()]
def sortPointsY(points): return points[:, points[2].argsort()]

# Lattice for a square
def pIn(x,y, Y): return x*Y + y
def pX(t, Y): return (abs(t) - (abs(t)%Y))//Y
def pY(t, Y): return abs(t)%Y
def genSquareTri(X, Y):
    Points = np.array([[x,y] for x in range(X+1) for y in range(Y+1)])
    Tris = glue(
        np.array([[pIn(pX(t, Y), pY(t, Y)+1, Y+1), pIn(pX(t, Y)+1, pY(t, Y)+1, Y+1), pIn(pX(t, Y)+1, pY(t, Y), Y+1)]
        if t >= 0 else
        [pIn(pX(t, Y), pY(t, Y), Y+1), pIn(pX(t, Y), pY(t, Y)+1, Y+1), pIn(pX(t, Y)+1, pY(t, Y), Y+1)]
        for t in range(-X*Y+1, X*Y)]),
        [0, 1, Y+1])
    return Points[:,0], Points[:,1], np.array(Tris)




__doc__ ="""

"[V]" indicates that the function works on arrays and not single objects.

## Utility functions
- crossiterate: cartesian product of two lists without the diagonal
- glue: stack array lines, given in a list, or stacks two array lines, given in succession
- getRandomPoints: returns an array of `n` random points of the form [somekey, 0:`rangex`, 0:`rangey`]^t

## Data structure manipulation
- point [V]: given a key and a position (vertical vector) returns [key, x, y]^t
- triangle [V]: given a key and a set of 3 point keys returns [key, p1, p2, p3]^t
- points2seg [V]: given two point keys returns [p1, p2]^t
- tri2seg [V]: inverse of seg2tri
- seg2tri [V]: given an array of keys and a 3 arrays of adjacent segments returns the corresponding array of triangles

## Graph stuff
- adjMatrix: returns the adjacency matrix of the lattice

## Sorting utility functions
- sortPointsK: sorts an array of points according to their keys
- sortPointsX: sorts an array of points according to their X-coordinate
- sortPointsY: sorts an array of points according to their Y-coordinate

# Lattice for a square
- genSquareTri: gives a uniform triangulation of a rectangle whose lower left corner is at (0,0) and whose upper right corner is at (`X`, `Y`).
    (uses a neat modulo trick)

"""
