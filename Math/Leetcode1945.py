class Solution:
    def getLucky(self, s: str, k: int) -> int:
        trans=""
        for c in s:
            trans+=str(ord(c)-ord('a')+1)
        for c in range(k):
            trans=self.transform(trans)

        return int(trans)

    def transform(self,trans):
        res=0
        for i in trans:
            res+=(ord(i)-ord('0'))
        return str(res)

if __name__ == '__main__':
    sol=Solution()
    # s = "iiii"
    # k = 1
    s = "leetcode"
    k = 2
    print(sol.getLucky(s,k))