class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        windows=dict()
        right=left=0
        res=0

        while right<len(s):
            c=s[right]
            right+=1
            windows[c]=windows[c]+1 if windows.get(c) else 1

            while windows[c]>1:
                d=s[left]
                left+=1
                windows[d]-=1
            res=max(res,right-left)
        return res

if __name__ == '__main__':
    sol=Solution()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))