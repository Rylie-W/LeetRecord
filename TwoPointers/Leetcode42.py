class Solution:
    def trap(self, height) -> int:
        if len(height) < 3:
            return 0
        trend = [0, 0]
        left = 0
        right = 1
        res = 0
        while right < len(height):
            c = height[right]
            right += 1
            # update
            temp=trend.copy()
            # temp = list()
            # temp.append(trend[0])
            # temp.append(trend[1])
            trend = self.update(trend, c, height[right - 2])
            if right == len(height) and trend == [1, 1]:
                trend = [0, 0]
                right+=1

            # need shrink
            if trend==[1,0] and temp==[0,1]:
                left=right-2
            if trend == [0, 0] and not temp == trend:
                res += self.count(left, right-1, height)
                left = right - 2
                trend=[1,0]
        return res

    def update(self, trend, cur, pre):
        if trend == [0, 0]:
            if cur > pre:
                trend = [0, 1]
            elif cur < pre:
                trend = [1, 0]

        elif trend == [1, 0]:
            if cur > pre:
                trend = [1, 1]

        elif trend == [1, 1]:
            if cur < pre:
                trend = [0, 0]

        elif trend == [0, 1]:
            if cur < pre:
                trend = [1, 0]

        return trend

    def count(self, left, right, height):
        h = min(height[left], height[right - 1])
        res = 0
        for i in range(left+1, right-1):
            res += (h - height[i])
        return res


if __name__ == '__main__':
    sol=Solution()
    # height=[0,1,0,2,1,0,1,3,2,1,2,1]
    height=[4,2,0,3,2,5]
    print(sol.trap(height))