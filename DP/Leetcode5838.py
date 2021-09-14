class Solution:
    def isPrefixString(self, s: str, words) -> bool:
        word=""
        index=0
        mark=0
        while len(word)<len(s):
            if index>=len(words):
                return False
            word+=words[index]
            if len(word)>len(s) or word!=s[:len(word)]:
                return False
            index+=1
        return True

if __name__ == '__main__':
    sol=Solution()
    s = "iloveleetcode"
    words = ["apples", "i", "love", "leetcode"]
    print(sol.isPrefixString(s,words))