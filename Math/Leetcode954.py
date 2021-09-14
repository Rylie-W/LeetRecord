import collections
class Solution:
    def canReorderDoubled(self, arr) -> bool:
        counter=collections.Counter(arr)
        # return self.dfs(counter,len(arr)/2)
        count=0
        arr.sort()
        for i in arr:
            if counter.get(i)>0:
                counter[i]-=1
                if counter.get(i*2) and counter.get(i*2)>0:
                    counter[i*2]-=1
                    count+=1
                    if count==len(arr)/2:
                        return True
                else:
                    counter[i]+=1

        return False
    # def dfs(self,counter,n):
    #     if n==0:
    #         return True
    #
    #     keys=list(counter.keys())
    #     keys.sort(key=lambda a:abs(a))
    #     for i in range(len(keys)):
    #         for j in keys[i:]:
    #             if j==keys[i]*2:
    #                 counter[keys[i]]-=1
    #                 if counter[j]>0:
    #                     counter[j]-=1
    #                 else:
    #                     continue
    #                 if counter[keys[i]]==0:
    #                     counter.pop(keys[i])
    #                 if counter.get(j)==0:
    #                     counter.pop(j)
    #                 if self.dfs(counter,n-1):
    #                     return True
    #
    #                 counter[keys[i]]=1+counter[keys[i]] if counter.get(keys[i]) else 1
    #                 counter[j] = 1 + counter[j] if counter.get(j) else 1
    #     return False

if __name__ == '__main__':
    sol=Solution()
    # arr=[0, 0]
    # arr = [3, 1, 3, 6]
    # arr = [4, -2, 2, -4]
    arr=[1,2,4,16,8,4]
    print(sol.canReorderDoubled(arr))

