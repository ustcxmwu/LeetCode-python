import math


class Solution:
    def minEatingSpeed(self, piles: 'List[int]', H: 'int') -> 'int':
        left = 0
        right = max(piles)
        while right - left > 1:
            mid_time = 0
            mid = math.ceil((left + right)/2)
            for elem in piles:
                mid_time += math.ceil(elem/mid)
            if mid_time > H:
                left = mid
            else:
                right = mid
        return right


if __name__=='__main__':
    solution = Solution()
    print(solution.minEatingSpeed([3,6,7,11], 8))
    print(solution.minEatingSpeed([30,11,23,4,20], 5))
    print(solution.minEatingSpeed([30,11,23,4,20], 6))
    a = 3
    print(a+3)
    print(a)