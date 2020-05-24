import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(math.sqrt(c))
        while i <= j:
            target = i*i + j*j
            if target == c:
                return True
            elif target < c:
                i += 1
            else:
                j -= 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.judgeSquareSum(2))