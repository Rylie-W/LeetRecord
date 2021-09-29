'''
# time limit exceeded
class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        res = 0
        left = right = 0
        largest, smallest = None, None
        li, si = 0, 0

        while right < len(nums):
            c = nums[right]
            right += 1
            largest = max(largest, c) if largest is not None else c
            li = right - 1 if largest == c else li
            smallest = min(smallest, c) if smallest is not None else c
            si = right - 1 if smallest == c else si
            dif = largest - smallest

            if dif > limit:
                if li > si:
                    left = si + 1
                    smallest = None
                    for i in range(left, right):
                        smallest = min(
                            smallest, nums[i]) if smallest else nums[i]
                        si = i if smallest == nums[i] else si
                else:
                    left = li + 1
                    largest = None
                    for i in range(left, right):
                        largest = max(largest, nums[i]) if largest else nums[i]
                        li = i if largest == nums[i] else li
            else:
                res = max(res, right - left)

            # flag=True
            # i=0
            # for i in range(left,right-1 if right-1 != left else right):
            #     if abs(nums[i]-c)>limit:
            #         flag=False
            #         break
            # if flag:
            #     res=max(res,right-left)
            # else:
            #     #shrink
            #     j=0
            #     for j in range(right-1,i,-1):
            #         if abs(nums[j]-c)>limit:
            #             flag=True
            #             break
            #     left=j+1 if flag else i+1
            #     res=max(res,right-left)
        return res
'''


class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        maxV = []
        minV = []
        left = right = 0
        res = 1
        while right < len(nums):
            c = nums[right]
            right += 1
            while len(maxV) > 0 and maxV[-1] < c:
                maxV.pop()
            maxV.append(c)
            while len(minV) > 0 and minV[-1] > c:
                minV.pop()
            minV.append(c)

            while maxV[0] - minV[0] > limit:
                if maxV[0] == nums[left]:
                    maxV.pop(0)
                if minV[0] == nums[left]:
                    minV.pop(0)
                left += 1

            res = max(res, right - left)
        return res


if __name__ == '__main__':
    sol = Solution()
    # nums = [8, 2, 4, 7]
    # limit = 4
    # nums = [10, 1, 2, 4, 7, 2]
    # limit = 5
    nums = [8, 2, 4, 7]
    limit = 4
    print(sol.longestSubarray(nums, limit))
