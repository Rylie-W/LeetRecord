# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        memo=[]
        while head is not None:
            memo.append(head)
            head=head.next
        left=0
        right=len(memo)-1
        temp=None
        while left<=right:
            if temp is not None:
                temp.next=memo[left]
            memo[left].next=memo[right]
            memo[right].next=None
            temp=right
            left+=1
            right-=1


