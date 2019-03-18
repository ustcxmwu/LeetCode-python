class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = list(str(x))
        ret = []
        for i in range(len(a)-1, -1, -1):
            ret.append(a[i])
        return ''.join(a) == ''.join(ret)


if __name__ == '__main__':
    print(str(-123))
    print(str(12))
    sol = Solution()
    print(sol.isPalindrome(-121))
    print(sol.isPalindrome(121))