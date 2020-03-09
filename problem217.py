from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(nums) == len(set(nums))


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    sol = Solution()
    print(sol.containsDuplicate(a))