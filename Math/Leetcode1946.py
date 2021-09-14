class Solution:
    def maximumNumber(self, num: str, change) -> str:
        res=""
        do=[False for i in change]
        for i,c in enumerate(change):
            if c>i:
                do[i]=True
        flag=0
        for i in range(len(num)):
            if flag==2:
                break
            if do[ord(num[i])-ord('0')]:
                flag=1
                res+=str(change[ord(num[i])-ord('0')])
                # if i<len(num)-1 and not do[ord(num[i+1])-ord('0')] and ord(num[i + 1]) - ord('0') != change[ord(num[i + 1]) - ord('0')]:
                    # and ord(num[i + 1]) - ord('0') != change[ord(num[i + 1]) - ord('0')]
                    # flag=2
            else:
                if flag==0 or (flag==1 and i<len(num)-1 and ord(num[i + 1]) - ord('0') == change[ord(num[i + 1]) - ord('0')]):
                    res+=num[i]
                else:
                    break
        res+=num[len(res):] if len(res)<len(num) else ""
        return res
if __name__ == '__main__':
    sol=Solution()
    # num = "021"
    # change = [9, 4, 3, 5, 7, 2, 1, 9, 0, 6]
    # num="132"
    # change=[9, 8, 5, 0, 3, 6, 4, 2, 6, 8]
    # num="214010"
    # change=[6, 7, 9, 7, 4, 0, 3, 4, 4, 7]
    # num="334111"
    # change=[0, 9, 2, 3, 3, 2, 5, 5, 5, 5]
    num="7218518888806706540"
    change=[5, 1, 5, 3, 1, 9, 5, 2, 0, 5]
    print(sol.maximumNumber(num,change))