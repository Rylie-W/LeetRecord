class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'

        pre='1'
