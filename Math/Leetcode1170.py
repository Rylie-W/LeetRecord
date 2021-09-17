import collections
class Solution:
    def numSmallerByFrequency(self, queries, words):
        def f(x):
            memo=collections.Counter(x)
            apha=list(memo.keys())
            apha.sort()
            return memo[apha[0]]

        w=list()
        for word in words:
            w.append(f(word))

        w.sort(reverse=True)
        res=list()
        for q in queries:
            count=0
            t=f(q)
            if t>w[0]:
                res.append(0)
            elif t<w[-1]:
                res.append(len(w))
            else:
                for i in range(len(w)):
                    if w[i]>t:
                        count+=1
                res.append(count)
        return res

if __name__ == '__main__':
    sol=Solution()
    # queries = ["bbb", "cc"]
    # words = ["a", "aa", "aaa", "aaaa"]
    # queries =["bba", "abaaaaaa", "aaaaaa", "bbabbabaab", "aba", "aa", "baab", "bbbbbb", "aab", "bbabbaabb"]
    # words =["aaabbb", "aab", "babbab", "babbbb", "b", "bbbbbbbbab", "a", "bbbbbbbbbb", "baaabbaab", "aa"]
    queries=["aabbabbb", "abbbabaa", "aabbbabaa", "aabba", "abb", "a", "ba", "aa", "ba", "baabbbaaaa", "babaa", "bbbbabaa"]
    words =["b", "aaaba", "aaaabba", "aa", "aabaabab", "aabbaaabbb", "ababb", "bbb", "aabbbabb", "aab", "bbaaababba", "baaaaa"]
    print(sol.numSmallerByFrequency(queries,words))