class Solution:
    def findSubstring(self, s: str, words):
        need=dict()
        do=dict()
        window=dict()
        for word in words:
            need[word]=1 if not need.get(word) else need[word]+1
            do[word[0]]=list(len(word)) if not do.get(word[0]) else do[word[0]]+[len(word)]

        left=right=valid=0
        res=list()
        while right<len(s):
            c=s[right]
            if do.get(c):
                for d in do[c]:
                    tr=right+d
                    

