class Solution:
    def sortArrayByParityII(self, nums):
        pre = next = 0
        while next < len(nums):
            if not(nums[next] % 2 == next % 2):
                pre = next
                next += 1
                while next < len(nums):
                    if not(nums[next] % 2 == next %
                           2) and nums[next] % 2 != nums[pre] % 2:
                        temp = nums[pre]
                        nums[pre] = nums[next]
                        nums[next] = temp
                        next = pre + 1
                        break
                    else:
                        next += 1
            next += 1
        return nums


if __name__ == '__main__':
    sol = Solution()
    # nums = [4, 2, 5, 7]
    # nums = [2, 3]
    # nums=[3,0,4,0,2,1,3,1,3,4]
    nums = [648, 831, 560, 986, 192, 424, 997, 829, 897, 843]
    print(sol.sortArrayByParityII(nums))
