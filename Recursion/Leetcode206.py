# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        #iteration
        '''
        pre=head
        cur=head.next
        pre.next=None

        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre
        '''
        def recurse(cur, pre):
            if cur.next==None:
                cur.next=pre
                return cur
            temp=cur.next
            cur.next=pre
            return recurse(temp,cur)
        pre=head
        cur=head.next
        return recurse(cur,pre)

