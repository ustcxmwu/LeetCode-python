# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        res = list()
        self.get_paths(root, [], res)
        return sum([int(item, 2) for item in res])

    def get_paths(self, root, path, res):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right:
            res.append("0b"+"".join([str(item) for item in path]))
        else:
            self.get_paths(root.left, path, res)
            self.get_paths(root.right, path, res)
        path.pop()


if __name__ == '__main__':
    root = TreeNode(1)
    l11 = TreeNode(0)
    l12 = TreeNode(1)
    root.left = l11
    root.right = l12
    l21 = TreeNode(0)
    l22 = TreeNode(1)
    l23 = TreeNode(0)
    l24 = TreeNode(1)
    l11.left = l21
    l11.right = l22
    l12.left = l23
    l12.right = l24
    sol = Solution()
    print(sol.sumRootToLeaf(root))
