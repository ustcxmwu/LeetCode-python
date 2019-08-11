class Solution:
    def isHappy(self, n: int) -> bool:
        result = set()
        while True:
            n = self.bit_sum(n)
            if n == 1:
                return True
            if n in result:
                return False
            else:
                result.add(n)

    def bit_sum(self, n: int):
        high = n // 10
        low = n % 10
        sum = low*low
        while high != 0:
            low = high % 10
            high = high // 10
            sum += low*low
        return sum


if __name__=='__main__':
    sol = Solution()
    ret = sol.isHappy(19)
    print(ret)