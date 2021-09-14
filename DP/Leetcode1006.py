class Solution:
    def minDominoRotations(self, tops, bottoms) -> int:
        for x in [tops[0],bottoms[0]]:
            if all(x in d for d in zip(tops,bottoms)):
                return len(tops)-max(tops.count(x),bottoms.count(x))
        return -1

if __name__ == '__main__':
    sol=Solution()
    # tops=[3,5,1,2,3]
    # bottoms=[3,6,3,3,4]
    # tops=[2,1,2,4,2,2]
    # bottoms=[5,2,6,2,3,2]
    tops=[1,2,1,1,1,2,2,2]
    bottoms=[2,1,2,2,2,2,2,2]
    print(sol.minDominoRotations(tops,bottoms))