from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t == 0 and len(set(nums)) == len(nums):
            return False
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums) and j-i <= k:
                if abs(nums[j] - nums[i]) <= t:
                    return True
                j = j+1
        return False

    def containsNearbyAlmostDuplicate2(self, nums: List[int], k: int, t: int) -> bool:
        for i in range(len(nums)):
            tmp = nums[i:i+k+1]
            for j in range(len(tmp)):
                for q in range(j+1, len(tmp)):
                    if abs(tmp[j] - tmp[q]) <= t:
                        return True
        return False


if __name__ == '__main__':
    nums = [2, 2]
    k = 3
    t = 0
    sol = Solution()
    print(sol.containsNearbyAlmostDuplicate(nums, k, t))

    a = [1, 2, 3, 4, 5]
    print(a[3:6])