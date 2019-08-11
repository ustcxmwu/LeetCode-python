class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for idx in range(n):
                nums1[idx] = nums2[idx]
        i = m - 1
        j = n - 1
        k = m + n - 1
        while j >= 0 and i >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i = i-1
            else:
                nums1[k] = nums2[j]
                j = j-1
            k = k-1
        while j >= 0:
            nums1[k] = nums2[j]
            k = k-1
            j = j-1



if __name__ == '__main__':
    sol = Solution()
    a = [2, 0]
    sol.merge(a, 1, [1], 1)
    print(a)