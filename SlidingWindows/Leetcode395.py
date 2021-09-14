class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # if len(s)<k:
        #     return 0
        # res=0
        # window=dict()
        # count=0
        # left=right=0
        # while right<len(s):
        #     c=s[right]
        #     right+=1
        #     if window.get(c):
        #         window[c]+=1
        #         if window[c]==k:
        #             count+=1
        #     else:
        #         window[c]=1
        #
        #     if count==len(window):
        #         res=max(res,right-left)
        #     #shrink
        if len(s)<k:
            return 0
        if k==1:
            return len(s)
        res = 0
        dp=[list() for i in s]
        dp[0].append(-1)
        dp[0].append(set(s[0]))
        for i in range(1,len(s)):
            if dp[i-1][0]>-1 and s[i] in dp[i-1][1]:
                dp[i].append(dp[i-1][0])
                dp[i].append(dp[i-1][1])
                res+=1
            else:
                res=max(res)

    # def helper(self,s,k,end):



    #     if len(s)<k:
    #         return 0
    #     res=len(s)+1
    #     for i in range(0,len(s)-k+1):
    #         t=self.helper(s,k,i)
    #         if t>-1:
    #             res=min(res,t)
    #     return res if res<len(s)+1 else 0
    # def helper(self,s,k,left):
    #     res=len(s)+1
    #     window=dict()
    #     count=0
    #     right=left
    #     while right<len(s):
    #         c=s[right]
    #         right+=1
    #         if window.get(c):
    #             window[c]+=1
    #             if window[c]==k:
    #                 count+=1
    #         else:
    #             window[c]=1
    #
    #         if count==len(window):
    #             return right-left
    #     return -1

if __name__ == '__main__':
    sol=Solution()
    # s = "aaabb"
    # k = 3
    s = "ababbc"
    k = 2
    print(sol.longestSubstring(s,k))