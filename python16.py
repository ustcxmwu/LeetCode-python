from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        _min = float("inf")
        _distance = float("inf")
        cur = 0

        while cur < len(nums) - 2:
            i = cur + 1
            j = len(nums) - 1
            while i < j:
                distance = abs(target - (nums[i] + nums[j] + nums[cur]))
                if _distance > distance:
                    _distance = distance
                    _min = nums[i] + nums[j] + nums[cur]

                if target > nums[i] + nums[j] + nums[cur]:
                    i += 1
                elif target < nums[i] + nums[j] + nums[cur]:
                    j -= 1
                else:
                    return nums[i] + nums[j] + nums[cur]

            cur += 1
        return _min


if __name__ == '__main__':
    a = [-1, 2, 1, -4]
    b = 1
    sol = Solution()
    print(sol.threeSumClosest(a, b))
