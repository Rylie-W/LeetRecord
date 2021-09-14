class Solution:
    def expressiveWords(self, s: str, words) -> int:
        schar=list()
        sindex=list()
        def mark():
            left=right=0
            while right<len(s):
                c=s[right]
                right+=1

                if c!=s[left]:
                    schar.append(s[left])
                    sindex.append(right-left-1)
                    left=right-1
                elif right==len(s):
                    schar.append(s[left])
                    sindex.append(right-left)
                if left==len(s)-1:
                    schar.append(s[left])
                    sindex.append(1)

        def match(s1,s2):
            if len(s1)>len(s2):
                return False
            left=right=0
            index=0
            while right<len(s1):
                c=s1[right]
                right+=1

                if c!=s1[left]:
                    count=sindex[index]-(right-left-1)
                    if not(count==0 or count>=2) or s1[left]!=schar[index]:
                        return False
                    left=right-1
                    index+=1
                elif right==len(s1):
                    count=sindex[index]-(right-left)
                    if not(count==0 or count>=2) or s1[left]!=schar[index]:
                        return False
                elif left==len(s1)-1:
                    if sindex[index]!=1 or s1[left]!=schar[index]:
                        return False
            if index!=len(schar)-1:
                return False
            return True



        mark()
        res=0
        for word in words:
            if match(word,s):
                res+=1
        return res

if __name__ == '__main__':
    sol=Solution()
    # s='zzzzzyyyyy'
    # words=['zzyy','zy','zyy']
    s='heeellooo'
    words=['hello','hi','helo']
    print(sol.expressiveWords(s,words))