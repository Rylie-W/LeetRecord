# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head, k: int):
        if head is None:
            return [None for i in range(k)]
        l=1
        p=head
        while p.next:
            l+=1
            p=p.next

        eachL=l//k
        more=l%k
        res=[]
        p=head
        for i in range(more):
            count=1
            start=p
            while count<eachL+1:
                p=p.next
                count+=1
            temp=p.next
            p.next=None
            p=temp
            res.append(start)
        for i in range(k-more):
            count=1
            start=p
            while count<eachL:
                p=p.next
                count+=1
            if p and p.next:
                temp=p.next
                p.next=None
                p=temp

            res.append(start)
        return res

