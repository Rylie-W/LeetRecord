class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(s)<len(p):
            return []
        need=dict()
        window=dict()
        count=0
        for i in p:
            need[i]=need[i]+1 if need.get(i) else 1
        left=right=0
        res=list()

        while right<len(s):
            c=s[right]
            right+=1
            if need.get(c)==None:
                left=right
                window=dict()
                count=0
            elif (window[c] == need[c] if window.get(c) else False):
                window[c]+=1
                while window[c]>need[c]:
                    window[s[left]]-=1
                    if window[s[left]]<need[s[left]] and window[s[left]]+1==need[s[left]]:
                        count-=1
                    left+=1
            else:
                window[c]=window[c]+1 if window.get(c) else 1
                if window[c]==need[c]:
                    count+=1
                if count==len(need):
                    res.append(left)
                    window[s[left]]-=1
                    left += 1
                    count-=1
        return res

if __name__ == '__main__':
    sol=Solution()
    s = "cbaebabacd"
    p = "abc"
    # s = "abab"
    # p = "ab"
    # s="vwwvv"
    # p="vwv"
    print(sol.findAnagrams(s,p))
