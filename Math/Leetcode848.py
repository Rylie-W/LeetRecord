class Solution:
    def shiftingLetters(self, temp: str, shifts) -> str:
        mod=26
        s=list()
        s[:0]=temp
        '''
        def shiftLetters(i,shift):
            for index in range(i+1):
                s[index]=chr((ord(s[index])-ord('a')+shift)%mod+ord('a'))
        for i,shift in enumerate(shifts):
            shiftLetters(i,shift)
        return ''.join(s)
        '''
        shift=0
        for i in range(len(shifts)-1,-1,-1):
            shift+=shifts[i]
            s[i]=chr((ord(s[i])-ord('a')+shift)%mod+ord('a'))

        return ''.join(s)

if __name__ == '__main__':
    # s=['a','b','c']
    # shifts=[3,5,9]
    s='aaa'
    shifts=[1,2,3]
    sol=Solution()
    print(sol.shiftingLetters(s,shifts))

