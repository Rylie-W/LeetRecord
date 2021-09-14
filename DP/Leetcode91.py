class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s)==0 or s[0]=='0':
            return 0
        if len(s)==1:
            return 1
        # dp=[0 for i in s]
        cur=1
        pre1=pre2=1

        for i in range(1,len(s)):
            temp=cur
            cur=0
            if s[i-1]!='0' and int(s[i-1]+s[i])<=26:
                # dp[i]+=dp[i-2] if i>1 else 1
                cur+=pre2

            if s[i]!='0':
                # dp[i]+=dp[i-1]
                cur+=pre1

            pre1=cur
            pre2=temp

        return cur

if __name__ == '__main__':
    sol=Solution()
    # s = "06"
    # s = "226"
    # s='10'
    print(sol.numDecodings(s))