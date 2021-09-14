class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder=preorder.split(',')
        stack=list()
        for i in preorder:
            stack.append(i)
            if not self.checkandRemove(stack):
                return False
        return True if len(stack)==1 and stack[0]=='#' else False

    def checkandRemove(self,stack):
        while len(stack)>2 and stack[-1]=='#' and stack[-2]=='#':
            if stack[-3]!="#":
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
            else:
                return False
        return True

if __name__ == '__main__':
    sol=Solution()
    preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    # preorder = "1,#"
    # preorder = "9,#,#,1"
    # preorder="9,#,92,#,#"
    print(sol.isValidSerialization(preorder))