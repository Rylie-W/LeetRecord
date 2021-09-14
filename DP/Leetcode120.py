class Solution:
    def minimumTotal(self, triangle) -> int:
        if len(triangle)==0:
            return 0

        dp=[triangle[0]]

        for s in range(1,len(triangle)):
            pre=dp[-1]
            cur=triangle[s]

            #first
            cur[0]+=pre[0]
            # dp=[cur[0]+dp[0]]+dp
            #last
            cur[-1]+=pre[-1]
            # dp.append(cur)

            for i in range(1,len(cur)-1):
                cur[i]+=min(pre[i-1],pre[i])

            dp.append(cur)

        return min(dp[-1])

if __name__ == '__main__':
    sol=Solution()
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(sol.minimumTotal(triangle))