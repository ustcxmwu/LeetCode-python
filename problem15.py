from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        ret = []
        for i in range(length):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            j, k = i+1, length-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ret.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return ret



if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    a = sol.threeSum(nums)
    print(a)
