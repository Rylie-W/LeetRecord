class Solution:
    def maxTurbulenceSize(self, arr) -> int:
        if len(arr)==0 or len(arr )==1:
            return len(arr)
        MORE='more'
        LESS='less'
        res=1
        right=1
        count=2
        flag=''
        while right<len(arr):
            if flag=='':
                while arr[right]==arr[right-1]:
                    right+=1
                    if right==len(arr):
                        return res
                if arr[right]<arr[right-1]:
                    flag=MORE
                if arr[right]>arr[right-1]:
                    flag=LESS
                # count+=1
            elif flag==MORE:
                if arr[right]<=arr[right-1]:
                    res=max(res,count)
                    count=2
                    flag=''
                    right-=1
                else:
                    count+=1
                    flag=LESS
            else:
                if arr[right]>=arr[right-1]:
                    res=max(res,count)
                    count=2
                    flag=''
                    right-=1
                else:
                    count+=1
                    flag=MORE
            right+=1
        return max(res,count)

if __name__ == '__main__':
    sol=Solution()
    # arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    # arr = [4, 8, 12, 16]
    arr=[9,9]
    # arr=[0,8,45,88,48,68,28,55,17,24]
    print(sol.maxTurbulenceSize(arr))



