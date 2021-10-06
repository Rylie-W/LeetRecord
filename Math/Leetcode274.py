import collections
class Solution:
    def hIndex(self, citations) -> int:
        count=collections.Counter(citations)
        keys=list(count.keys())
        h=max(keys)
        minmum=min(keys)
        memo=0
        while h>=minmum:
            if count.get(h) is not None:
                memo+=count[h]
            if memo>=h:
                return h
            h-=1
        return memo if memo<h else -1
if __name__ == '__main__':
    sol=Solution()
    # citations = [3, 0, 6, 1, 5]
    # citations = [1, 3, 1]
    citations=[100]
    print(sol.hIndex(citations))