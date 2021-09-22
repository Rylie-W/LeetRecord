class Solution:
    def maxLength(self, arr) -> int:
        def helper(word):
            temp=[]
            temp[:0]=word
            res=set()
            for w in temp:
                if w not in res:
                    res.add(w)
                else:
                    return None
            return res

        memo=[]
        for a in arr:
            temp=helper(a)
            if temp is not None:
                memo.append(temp)
        memo.sort(key=lambda a:len(a),reverse=True)
        def dfs(index,path):
            # if len(memo[index])*(len(memo)-index)<=res:
            #     return -1
            if index==len(memo):
                return 0

            res=0
            for i in range(index,len(memo)):
                if len(path|memo[i])==len(path)+len(memo[i]):
                    res=max(res,len(memo[i])+dfs(i+1,path|memo[i]))
            return res

        return dfs(0,set())

if __name__ == '__main__':
    sol=Solution()
    arr = ["un", "iq", "ue"]
    # arr = ["cha", "r", "act", "ers"]
    # arr = ["abcdefghijklmnopqrstuvwxyz"]
    # arr=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
    print(sol.maxLength(arr))



