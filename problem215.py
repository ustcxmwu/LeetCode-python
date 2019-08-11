class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        i = 0
        count = len(nums)
        while i < k:
            for j in range(count - i):
                if nums[j] > nums[count - i - 1]:
                    t = nums[j]
                    nums[j] = nums[count - i - 1]
                    nums[count - i - 1] = t
            i = i+1
        return nums[count - k]



if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthLargest([3,2,1,5,6,4], 2))