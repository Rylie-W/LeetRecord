class Solution:
    def camelMatch(self, queries, pattern: str) :
        res=[]
        def match(q):
            j=0
            for i in range(len(q)):
                if j<len(pattern) and q[i]==pattern[j]:
                    j+=1
                elif q[i]>='A' and q[i]<='Z':
                    return False
            return j==len(pattern)


        for q in queries:
            res.append(match(q))
        return res

