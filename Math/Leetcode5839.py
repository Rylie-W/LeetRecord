import math
import heapq
class Solution:
    def minStoneSum(self, piles, k: int) -> int:
        q=list()
        for i in piles:
            heapq.heappush(q,i)
        while k:
            c=q[-1]
            q.pop()
            c=c-math.floor(c/2)
            heapq.heappush(q,c)
            k-=1

        res=0
        for i in q:
            res+=i
        return res

if __name__ == '__main__':
    sol=Solution()
    piles = [4, 3, 6, 7]
    k = 3
    print(sol.minStoneSum(piles,k))