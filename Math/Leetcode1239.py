class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ""
        for i in range(len(palindrome)//2+1):
            if palindrome[i]!='a':
                if i==len(palindrome)//2:
                     # if i+2<len(palindrome):
                     if len(palindrome)%2==1:
                         if palindrome[i+1]!='a':
                            # return palindrome[:i + 1] + chr(ord(palindrome[i]) - 1) + palindrome[i + 2:]
                            return palindrome[:i + 1] + 'a' + palindrome[i + 2:]
                         else:
                             return palindrome[:i + 1] + 'b' + palindrome[i + 2:]
                     else:
                         # if palindrome[i]!='a':
                         #    return palindrome[:i + 1] + chr(ord(palindrome[i]) - 1)
                         # else:
                         return palindrome[:i] + 'b'+palindrome[i+1:]
                else:
                    # return palindrome[:i]+chr(ord(palindrome[i])-1)+palindrome[i+1:]
                    return palindrome[:i] + 'a' + palindrome[i + 1:]
        return palindrome[0]+'b'+palindrome[2:]
if __name__ == '__main__':
    sol=Solution()
    palindrome = "abccba"
    # palindrome = "a"
    # palindrome = "aa"
    # palindrome ="aba"
    print(sol.breakPalindrome(palindrome))
