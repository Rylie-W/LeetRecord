class Solution:
    def calculate(self, s: str) -> int:
        stack=list()
        for i in s:
            if i==" ":
                continue
            if i==")":
                temp=""
                while stack[-1]!="(":
                    temp=stack[-1]+temp
                    stack.pop()
                stack.pop()
                stack.append(str(self.helper(temp)))
            else:
                stack.append(i)
        return self.helper("".join(stack))
    def helper(self,s):
        i=0
        while i <len(s):
            if i-1>-1 and (s[i]=='+' or s[i]=='-') and s[i-1]!='-' and s[i-1]!='+':
                s=s[:i]+'#'+s[i:]
                i+=2
            elif i-1>-1 and s[i-1]=='-' and s[i]=='-':
                s=s[:i-1]+'+'+s[i+1:]
            elif i-1>-1 and s[i-1]=='-' and s[i]=='+':
                s=s[:i-1]+'-'+s[i+1:]
            elif i-1>-1 and s[i-1]=='+' and s[i]=='-':
                s=s[:i-1]+'-'+s[i+1:]
            elif i-1>-1 and s[i-1]=='+' and s[i]=='+':
                s=s[:i-1]+'+'+s[i+1:]
            else:
                i+=1
        nums=[int(x) for x in s.split("#") if x!='']
        return sum(nums)

if __name__ == '__main__':
    sol=Solution()
    # s="-1+1"
    # s = " 2-1 + 2 "
    # s = "(1+(4+5+2)-3)+(6+8)"
    s="2-(5-6)"
    print(sol.calculate(s))

