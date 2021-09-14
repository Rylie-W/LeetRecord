import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        memo=set()
        i=0
        squ=i*i
        memo.add(squ)

        while squ<=c/2:
            remain=c-squ
            temp=pow(int(math.sqrt(remain)),2)
            if remain in memo or remain==temp:
                return True

            memo.add(temp)
            i+=1
            squ=i*i
        return False

if __name__ == '__main__':
    sol=Solution()
    c=1
    print(sol.judgeSquareSum(c))