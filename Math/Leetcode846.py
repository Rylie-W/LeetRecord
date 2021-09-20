import collections
class Solution:
    def isNStraightHand(self, hand, groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        hand=collections.Counter(hand)
        for i in sorted(hand):
            if hand[i]>0:
                for j in range(1,groupSize):
                    hand[i+j]-=hand[i]
                    if hand[i+j]<0:
                        return False
                hand[i]=0
        return True

if __name__ == '__main__':
    sol=Solution()
    # hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    # groupSize = 3
    # hand = [1, 2, 3, 4, 5]
    # groupSize = 4
    hand=[9, 13, 15, 23, 22, 25, 4, 4, 29, 15, 8, 23, 12, 19, 24, 17, 18, 11, 22, 24, 17, 17, 10, 23, 21, 18, 14, 18, 7, 6,
     3, 6, 19, 11, 16, 11, 12, 13, 8, 26, 17, 20, 13, 19, 22, 21, 27, 9, 20, 15, 20, 27, 8, 13, 25, 23, 22, 15, 9, 14,
     20, 10, 6, 5, 14, 12, 7, 16, 21, 18, 21, 24, 23, 10, 21, 16, 18, 16, 18, 5, 20, 19, 20, 10, 14, 26, 2, 9, 19, 12,
     28, 17, 5, 7, 25, 22, 16, 17, 21, 11]
    groupSize =10
    print(sol.isNStraightHand(hand,groupSize))