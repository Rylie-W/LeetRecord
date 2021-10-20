class Solution:
    def reverseWords(self, s: str) -> str:
        s=[i for i in s]
        def reverse(s,l,r):
            while l<r:
                temp=s[l]
                s[l]=s[r]
                s[r]=temp
                l+=1
                r-=1
        l=0
        while s[l]==' ':
            l+=1
        r=len(s)-1
        while s[r]==' ':
            r-=1
        s=s[l:r+1]
        reverse(s,0,len(s)-1)
        l=r=0
        while r<len(s):
            if s[r]!=' ':
                r+=1
                if r==len(s):
                    reverse(s,l,r-1)
            else:
                reverse(s,l,r-1)
                temp=r
                r+=1
                while r<len(s) and s[r]==' ':
                    r+=1
                s=s[:temp+1]+s[r:]
                r=temp+1
                l=r
        return ''.join(s)
        # temp=s.split(" ")
        # s=list()
        # for t in temp:
        #     if t!='':
        #         s.append(t)
        # left=0
        # right=len(s)-1
        # while left<right:
        #     temp=s[left]
        #     s[left]=s[right]
        #     s[right]=temp
        #     left+=1
        #     right-=1
        # res=""
        # for i in range(len(s)):
        #     if i==len(s)-1:
        #         res+=s[i]
        #     else:res+=s[i]+' '
        # return res


if __name__ == '__main__':
    sol=Solution()
    # s = "  hello world  "
    # s = "the sky is blue"
    s="a good   example"
    print(sol.reverseWords(s))