class Solution:
    def slowestKey(self, releaseTimes, keysPressed: str) -> str:
        res=0
        for i in range(1,len(releaseTimes)):
            if res==0:
                if releaseTimes[i]-releaseTimes[i-1]>releaseTimes[0]:
                    res=i
                elif releaseTimes[i]-releaseTimes[i-1]==releaseTimes[0] and keysPressed[i]>keysPressed[0]:
                    res=i
            else:
                if releaseTimes[i]-releaseTimes[i-1]> releaseTimes[res]-releaseTimes[res-1]:
                    res=i
                elif releaseTimes[i]-releaseTimes[i-1]==releaseTimes[res]-releaseTimes[res-1] and keysPressed[i]>keysPressed[res]:
                    res=i

        return keysPressed[res]

if __name__ == '__main__':
    sol=Solution()
    releaseTimes = [9, 29, 49, 50]
    keysPressed = "cbcd"
    print(sol.slowestKey(releaseTimes,keysPressed))