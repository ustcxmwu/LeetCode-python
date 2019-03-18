class Solution:
    def reverse(self, x: int) -> int:
        if x<-2**31 or x>2**31-1:
            return 0
        ret = 0
        t = x if x >= 0 else -x
        while t//10 != 0:
            ret = ret*10 + t % 10
            t = t//10
        if t != 0:
            ret = ret*10 + t
        if ret<-2**31 or ret>2**31-1:
            return 0
        return ret if x >= 0 else -ret


if __name__ == "__main__":
    print(5%10)
    print(4//11)
    sol = Solution()
    print(sol.reverse(123))
    print(sol.reverse(-123))
    print(sol.reverse(120))
    print(sol.reverse(0))