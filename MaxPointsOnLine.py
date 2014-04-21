'''
Created on Mar 18, 2014

@author: C_TLU
'''
#Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1
        max_val = 0
        max_val_all = 0
        max_int = 2147483647
        comp = 0
        for i in range(len(points)):
            slop = {}
            for j in range(len(points)):
                if i != j:
                    if (points[i].x != points[j].x) or (points[i].y != points[j].y):
                        if (points[i].x != points[j].x):
                            k = (float(points[i].y)-float(points[j].y))/(float(points[i].x)-float(points[j].x))
                        else:
                            k = max_int
                        if slop.has_key(k):
                            slop[k] = slop[k] +1
                        else:
                            slop[k] = 1
                        if slop[k]>max_val:
                            max_val = slop[k]
                    else:
                        comp = comp + 1
            if (1 + max_val + comp) > max_val_all:
                max_val_all = 1 + max_val + comp
            comp = 0
            max_val = 0
            del slop
        return max_val_all