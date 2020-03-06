# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        first = l1
        second = l2
        if first.val <= second.val:
            head = ListNode(first.val)
            first = first.next
        else:
            head = ListNode(second.val)
            second = second.next
        tail = head
        while True:
            if not first:
                while second:
                    tail.next = ListNode(second.val)
                    second = second.next
                    tail = tail.next
                break
            if not second:
                while first:
                    tail.next = ListNode(first.val)
                    first = first.next
                    tail = tail.next
                break
            if first.val <= second.val:
                tail.next = ListNode(first.val)
                tail = tail.next
                first = first.next
            else:
                tail.next = ListNode(second.val)
                tail = tail.next
                second = second.next
        return head




if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    c = ListNode(4)
    b.next = c

    d = ListNode(1)
    e = ListNode(3)
    d.next = e
    f = ListNode(4)
    e.next = f

    m = Solution().mergeTwoLists(a, d)
    while m:
        print(m.val)
        m = m.next



