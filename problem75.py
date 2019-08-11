class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {0:0, 1:0, 2:0}
        for i in nums:
            if nums[i] == 0:
                count[0] = count[0] + 1
            if nums[i] == 1:
                count[1] = count[1] + 1
            if nums[i] == 2:
                count[2] = count[2] + 1
        for idx in range(len(nums)):
            if idx < count[0]:
                nums[idx] = 0
            elif idx < count[0] + count[1]:
                nums[idx] = 1
            else:
                nums[idx] = 2





if __name__ == '__main__':
    a = [1, 2, 3]
    # a[0:1:1] = 4
    print(a[0:1:1])