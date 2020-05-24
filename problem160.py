

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A = []
        ta = headA
        while ta:
            A.append(ta.val)
            ta = ta.next
        B = []
        tb = headB
        while tb:
            B.append(tb.val)
            tb = tb.next
        while A and B:
            if A.pop() != B.pop():
                break
        condi = headA
        for i in range(len(A) + 1):
            condi = headA.next

        return condi
