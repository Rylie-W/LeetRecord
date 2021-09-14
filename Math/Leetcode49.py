class Solution:
    def groupAnagrams(self, strs):
        if not strs or len(strs)==0:
            return strs

        memo=dict()
        for i in strs:
            temp=self.sortString(i)
            if memo.get(temp):
                memo[temp].append(i)
            else: memo[temp]=[i]

        return memo.values()

    def sortString(self,s):
        sorted_s=sorted(s)
        return ''.join(sorted_s)

if __name__ == '__main__':
    sol=Solution()
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs=['','']
    print(sol.groupAnagrams(strs))
