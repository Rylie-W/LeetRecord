class Solution:
    def maxCount(self, m: int, n: int, ops) -> int:
        if len(ops)==0:
            return m*n
        x=m
        y=n
        for o in ops:
            x=min(x,o[0])
            y=min(y,o[1])
        return x*y

