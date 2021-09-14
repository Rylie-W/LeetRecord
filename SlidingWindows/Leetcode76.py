class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=dict()
        window=dict()
        for c in t:
            need[c]=1 if not need.get(c) else need[c]+1
        valid=left=right=0
        res=""
        while right<len(s):
            c=s[right]
            right+=1
            if need.get(c):
                window[c]=1 if not window.get(c) else window[c]+1
                if window[c]==need[c]:
                    valid+=1

            while valid==len(need):
                res=s[left:right] if right-left<len(res) or res=="" else res
                d=s[left]
                left+=1
                if need.get(d):
                    window[d]-=1
                    if window[d]<need[d]:
                        valid-=1
        return res

if __name__ == '__main__':
    sol=Solution()
    # s = "ADOBECODEBANC"
    # t = "ABC"
    s = "a"
    t = "aa"
    print(sol.minWindow(s,t))