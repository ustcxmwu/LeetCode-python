# Definition for a binary tree node.

import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = collections.deque()
        queue.append((root, 1))
        res = 0
        while queue:
            width = queue[-1][1] - queue[0][1] + 1
            res = max(width, res)
            length = len(queue)
            for _ in range(length):
                n, c = queue.popleft()
                if n.left:
                    queue.append((n.left, c * 2))
                if n.right:
                    queue.append((n.right, c * 2 + 1))
        return res