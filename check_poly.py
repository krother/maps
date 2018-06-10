"""
Check whether a point is inside a polygon
"""
import matplotlib.path as mplPath
import numpy as np

path = mplPath.Path(np.array([
       (10, 10), (100, 10), (100, 70), (10, 70)
    ], dtype=np.float32))

assert path.contains_point((11, 11))
assert not path.contains_point((200, 100))
assert path.contains_point((90, 50))
assert not path.contains_point((110, 50))
assert path.contains_point((80, 60))
assert not path.contains_point((60, 80))


# source: https://stackoverflow.com/questions/16625507/python-checking-if-point-is-inside-a-polygon#16627234
