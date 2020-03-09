from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        for idx, value in enumerate(nums):
            if idx == 0 and value > nums[idx+1]:
                return idx
            elif idx == len(nums) - 1 and value > nums[idx-1]:
                return idx
            else:
                if nums[idx-1] < value > nums[idx+1]:
                    return idx



