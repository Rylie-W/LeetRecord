# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        p1=l1
        p2=l2
        count=0
        while p1 and p2:
            count+=p1.val
            count+=p2.val
            p1.val=count%10
            count=count//10
            p2=p2.next
            if p1.next is None:
                p1.next=p2
                p1=None
            else:
                p1=p1.next
        while p2 and count>0:
            count+=p2.val
            p2.val=count%10
            count=count//10
            if p2.next is None and count>0:
                p2.next=ListNode(count)
                break
            else:
                p2=p2.next

        while p1 and count:
            count += p1.val
            p1.val = count % 10
            count = count // 10
            if p1.next is None and count > 0:
                p1.next = ListNode(count)
                break
            else:
                p1 = p1.next

        return l1
