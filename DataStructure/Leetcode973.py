from collections import deque
class Solution:
    def kClosest(self, points, k: int):
        def getDistence(x,y):
            return x**2+ y**2
        q=deque()
        d=deque()
        for x,y in points:
            cur_distance=getDistence(x,y)
            while len(d)>=k and d[-1]>cur_distance:

