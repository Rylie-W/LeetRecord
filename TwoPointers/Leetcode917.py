class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        left=0
        right=len(s)-1
        def isChar(a):
            return (ord(a)>=ord('a') and ord(a)<=ord('z')) or (ord(a)>=ord('A') and ord(a)<=ord('Z'))
        while left<right:
            if isChar(s[left]) and isChar(s[right]):
                temp=s[left]
                s[left]=s[right]
                s[right]=temp
                left+=1
                right-=1
            while not isChar(s[left]):
                left+=1
                if left>=right:
                    return ''.join(s)
            while not isChar(s[right]):
                right-=1
                if right<=left:
                    return ''.join(s)

        return ''.join(s)

if __name__ == '__main__':
    sol=Solution()
    # s = "a-bC-dEf-ghIj"
    s = "Test1ng-Leet=code-Q!"
    print(sol.reverseOnlyLetters(s))