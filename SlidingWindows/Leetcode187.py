class Solution:
    def findRepeatedDnaSequences(self, s: str):
        if len(s) <= 10:
            return list()
        window = dict()
        res = list()
        left = 0
        while left + 9 < len(s):
            c = s[left:left + 10] if left + 10 < len(s) else s[left:]
            left += 1
            if window.get(c):
                window[c] += 1
                if window[c] == 2:
                    res.append(c)
            else:
                window[c] = 1
        return res

if __name__ == '__main__':
    sol=Solution()
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(sol.findRepeatedDnaSequences(s))