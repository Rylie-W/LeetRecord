class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
            if k ==1:
                res=""
                for i in range(len(s)):
                    res=min(res,s[i:]+s[:i]) if res!="" else s[i:]+s[:i]
                return res
            else:
                sorted(s,key=lambda a:a)
                return s
