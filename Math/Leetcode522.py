class Solution:
    def findLUSlength(self, strs) -> int:
        strs.sort(key=lambda a:len(a),reverse=True)
        def isSubString(w1,w2):
            i=0
            for c in w2:
                if i<len(w1) and w1[i]==c:
                    i+=1
            return i==len(w1)

        for i,w1 in enumerate(strs):
            if all(not isSubString(w1,w2) for j,w2 in enumerate(strs) if j!=i):
                return len(w1)

        return -1





if __name__ == '__main__':
    sol=Solution()
    # strs = ["aba", "cdc", "eae"]
    strs = ["aaa", "aaa", "aa"]
    print(sol.findLUSlength(strs))
