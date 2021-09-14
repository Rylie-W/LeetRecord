class Solution:
    def maxArea(self, height) -> int:
        left=0
        right=len(height)-1
        res=min(height[left],height[right])*(right-left)

        while right>left:
            res=max(res,(right-left)*min(height[right],height[left]))
            if height[left]<height[right]:
                left+=1
            else: right-=1
        return res

if __name__ == '__main__':
    sol=Solution()
    # height = [1, 1]
    height=[1,3,2,5,25,24,5]
    print(sol.maxArea(height))
