from typing import List


def median(nums: List[int]) -> float:
    if len(nums) % 2 == 0:
        return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2.0
    else:
        return float(nums[len(nums) // 2])


#
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         if len(nums1) == 0:
#             if len(nums2) == 0:
#                 return 0.0
#             else:
#                 return median(nums2)
#         else:
#             if len(nums2) == 0:
#                 return median(nums1)
#         i = 0
#         j = 0
#         tmp = list()
#         while True:
#             if nums1[i] <= nums2[j]:
#                 tmp.append(nums1[i])
#                 i += 1
#                 if i == len(nums1):
#                     tmp.extend(nums2[j::])
#                     break
#             else:
#                 tmp.append(nums2[j])
#                 j += 1
#                 if j == len(nums2):
#                     tmp.extend(nums1[i::])
#                     break
#         return median(tmp)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        if len(nums2) == 0:
            return (nums1[(len(nums1) - 1) // 2] + nums1[len(nums1) // 2]) / 2
        left, right = 0, 2 * len(nums2)
        while left <= right:
            mid2 = (left + right) // 2
            mid1 = len(nums1) + len(nums2) - mid2
            l1 = float("-inf") if mid1 == 0 else nums1[(mid1 - 1) // 2]
            l2 = float("-inf") if mid2 == 0 else nums2[(mid2 - 1) // 2]
            r1 = float("inf") if mid1 == len(nums1) * 2 else nums1[mid1 // 2]
            r2 = float("inf") if mid2 == len(nums2) * 2 else nums2[mid2 // 2]
            if l1 > r2:
                left = mid2 + 1
            elif l2 > r1:
                right = mid2 - 1
            else:
                return (max(l1, l2) + min(r1, r2)) / 2


if __name__ == '__main__':
    a = [1, 2]
    b = [-1, 3]
    sol = Solution()
    print(sol.findMedianSortedArrays(a, b))
