# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        pre,cur=head,head
        while pre is not None and pre.next is not None:
            pre=pre.next.next if pre.next is not None else pre.next
            cur=cur.next
        return cur