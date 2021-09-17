class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        res=[]
        while popped:
            top=popped[0]
            popped.pop(0)
            if len(res)==0 or top!=res[-1]:
                if len(pushed) == 0:
                    return False
                while pushed[0]!=top:
                    res.append(pushed[0])
                    pushed.pop(0)
                    if len(pushed)==0:
                        return False
                pushed.pop(0)
            elif top==res[-1]:
                res.pop()
            else:
                return False
        return True

if __name__ == '__main__':
    sol=Solution()
    # pushed = [1, 2, 3, 4, 5]
    # popped = [4, 5, 3, 2, 1]
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    print(sol.validateStackSequences(pushed,popped))

