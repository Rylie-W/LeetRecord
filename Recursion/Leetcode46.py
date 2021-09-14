class Solution:
    def permute(self, nums):
        if len(nums)<2:
            return nums

        # q=[[num] for num in nums]
        # visited=[{i} for i in range(len(nums))]
        q=list()
        visited=list()
        for num in nums:

        depth=1

        while depth<len(nums):
            size=len(q)

            for s in range(size):
                cur=q[0]
                v=visited[0]

                q.pop(0)
                visited.pop(0)

                for i in range(len(nums)):
                    if i not in v:
                        q.append(cur+[nums[i]])
                        visited.append(v.union({i}))
            depth+=1
        return q

if __name__ == '__main__':
    sol=Solution()
    nums = [1,1,2]
    print(sol.permute(nums))