from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        count = [0] * 31
        for i in range(31):
            for num in nums:
                if num >> i & 1 == 1:
                    count[i] += 1
        total = []
        for c in count:
            total.append(c * (len(nums) - c))
        return sum(total)


if __name__ == '__main__':
    a = [6, 1, 8, 6, 8]
    sol = Solution()
    print(sol.totalHammingDistance(a))
