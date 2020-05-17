# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        tail = None
        while head:
            cur = head
            head = head.next
            cur.next = tail
            tail = cur
        return tail


if __name__ == '__main__':
    print()


