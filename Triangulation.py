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
def tri2seg(tris): return {tris[0][n] : {(tris[1+a][n], tris[1+a+b][n]) for a in range(2) for b in range(1, 3-a)} for n in range(tris.shape[1])}
def seg2tri(keys, seg1, seg2, seg3): return triangle(keys, np.array([np.fromiter((x for x in set(p)), int) for p in glue([seg1,seg2,seg3]).reshape(1,6)]).T)

# Graph stuff
def adjMatrix(edgeset): return nx.to_numpy_array(nx.from_edgelist(edgeset))

# For Sorting-based algorithms
def sortPointsK(points): return points[:, points[0].argsort()]
def sortPointsX(points): return points[:, points[1].argsort()]
def sortPointsY(points): return points[:, points[2].argsort()]

# Lattice for a square
def genTri(x,y,isBottom): return ((x,y),(x+1,y),(x,y+1)) if isBottom else ((x,y+1),(x+1,y),(x+1,y+1))
def sqlattice(X,Y): return {genTri(x,y,isBottom) for x in range(X) for y in range(Y) for isBottom in range(2)}




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
- tri2seg [V]: given an array of triangles returns the dict of the form of triangleKey : setOfSegments
- seg2tri [V]: given an array of keys and a 3 arrays of adjacent segments returns the corresponding array of triangles

## Graph stuff
- adjMatrix: returns the adjacency matrix of the lattice

## Sorting utility functions
- sortPointsK: sorts an array of points according to their keys
- sortPointsX: sorts an array of points according to their X-coordinate
- sortPointsY: sorts an array of points according to their Y-coordinate

"""
