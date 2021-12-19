class Solution:
    def decodeString(self, s: str) -> str:
        stack=list()
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                temp=list()
                multi=0
                count=0
                while ( len(stack)>0 and stack[-1]>='a' and stack[-1]<='z'):
                    temp=[stack[-1]]+temp
                    stack.pop()
                if stack[-1]=='[':
                    stack.pop()
                while (len(stack)>0 and stack[-1]>='0' and stack[-1]<='9'):
                    multi+=int(stack[-1])*10**count
                    stack.pop()
                    count+=1
                temp=temp*multi if multi>0 else temp
                stack+=temp

        return ''.join(stack)

if __name__ == '__main__':
    sol=Solution()
    # s = "2[abc]3[cd]ef"
    s="2[20[bc]31[xy]]xd4[rt]"
    print(sol.decodeString(s))
