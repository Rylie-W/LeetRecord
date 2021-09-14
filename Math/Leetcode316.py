import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        memo=collections.Counter(s)
        stack=list()
        visited=dict()

        for i in range(len(s)):
            memo[s[i]]-=1
            if not(visited.get(s[i],-1)==-1 or visited.get(s[i],-1)==False):
                continue
            else:
                while len(stack)>0 and s[i]<stack[-1] and memo[stack[-1]]>0:
                    visited[stack[-1]]=False
                    stack.pop()
                stack.append(s[i])
                visited[s[i]]=True

        res=''
        for i in stack:
            res+=i
        return res

if __name__ == '__main__':
    sol=Solution()
    s = "bcabc"
    # s = "cbacdcbc"#acdb
    print(sol.removeDuplicateLetters(s))
