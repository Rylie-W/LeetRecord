import collections
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count=collections.Counter(text)
        res=-1
        for i in ['b','a','l','o','n']:
            if i=='l' or i=='o':
                count[i]=int(count[i]/2)
            res=count[i] if res==-1 else min(res,count[i])
        return res

if __name__ == '__main__':
    sol=Solution()
    text = "nlaebolko"
    print(sol.maxNumberOfBalloons(text))