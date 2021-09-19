class Solution:
    def reverseWords(self, s: str) -> str:
        temp=s.split(" ")
        s=list()
        for t in temp:
            if t!='':
                s.append(t)
        left=0
        right=len(s)-1
        while left<right:
            temp=s[left]
            s[left]=s[right]
            s[right]=temp
            left+=1
            right-=1
        res=""
        for i in range(len(s)):
            if i==len(s)-1:
                res+=s[i]
            else:res+=s[i]+' '
        return res


if __name__ == '__main__':
    sol=Solution()
    s = "  hello world  "
    print(sol.reverseWords(s))