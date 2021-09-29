class Solution:
    def minSumOfLengths(self, arr, target: int) -> int:
        res = []
        for i in range(len(arr)):
            right=i
            count=0
            while right<len(arr):
                count+=arr[right]
                right+=1
                if count==target:
                    if len(res) == 0:
                        res.append(right - i)
                    elif len(res) == 1:
                        if right - i > res[0]:
                            res.append(right - i)
                        else:
                            res = [right - i] + res
                    else:
                        if right - i < res[0]:
                            res = [right - i] + res
                            res.pop()
                        elif right - i < res[-1]:
                            res.pop()
                            res.append(right - i)
        # left = right = 0
        # count = 0
        # while right < len(arr):
        #     c = arr[right]
        #     right += 1
        #     count += c
        #     if count == target:
        #         if len(res) == 0:
        #             res.append(right - left)
        #         elif len(res) == 1:
        #             if right - left > res[0]:
        #                 res.append(right - left)
        #             else:
        #                 res = [right - left] + res
        #         else:
        #             if right - left < res[0]:
        #                 res = [right - left] + res
        #                 res.pop()
        #             elif right - left < res[-1]:
        #                 res.pop()
        #                 res.append(right - left)
        #         left = right
        #         count = 0
        #     elif count > target:
        #         while count > target and left < len(arr):
        #             count -= arr[left]
        #             left += 1
        #         if count == target:
        #             if len(res) == 0:
        #                 res.append(right - left)
        #             elif len(res) == 1:
        #                 if right - left > res[0]:
        #                     res.append(right - left)
        #                 else:
        #                     res = [right - left] + res
        #             else:
        #                 if right - left < res[0]:
        #                     res = [right - left] + res
        #                     res.pop()
        #                 elif right - left < res[-1]:
        #                     res.pop()
        #                     res.append(right - left)
        #             left = right
        #             count = 0

        return sum(res) if len(res) == 2 else -1


if __name__ == '__main__':
    sol = Solution()
    # arr = [3, 2, 2, 4, 3]
    # target = 3
    # arr = [4, 3, 2, 6, 2, 3, 4]
    # target = 6
    # arr = [1, 2, 2, 3, 2, 6, 7, 2, 1, 4, 8]
    # target = 5
    arr=[2, 1, 3, 3, 2, 3, 1]
    target=6
    print(sol.minSumOfLengths(arr, target))
