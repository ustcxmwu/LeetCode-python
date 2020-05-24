from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos = [-1, -1]
        for idx, num in enumerate(nums):
            if num == target:
                pos[0] = idx
                for right in range(idx, len(nums)):
                    if nums[right] == target:
                        pos[1] = right
                break
        return pos


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    sol = Solution()
    print(sol.searchRange(nums, 6))