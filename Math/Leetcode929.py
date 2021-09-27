class Solution:
    def numUniqueEmails(self, emails) -> int:
        def helper(email):
            res=""
            ignore=False
            domain=False
            for c in email:
                if ignore:
                    if c=='@':
                        domain=True
                        res+=c
                        ignore=False
                else:
                    if domain:
                        res+=c
                    else:
                        if c=='+':
                            ignore=True
                        elif c=='@':
                            res+=c
                            domain=True
                        elif c!='.':
                            res+=c
            return res

        res=set()
        for e in emails:
            res.add(helper(e))
        return len(res)

if __name__ == '__main__':
    sol=Solution()
    emails=["test.email+alex@leetcode.com", "test.email@leetcode.com"]
    # emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    # emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    print(sol.numUniqueEmails(emails))