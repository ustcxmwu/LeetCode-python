class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        short = nums1 if len(nums1) <= len(nums2) else nums2
        long = nums1 if len(nums1) > len(nums2) else nums2
        ret = []
        for elem in short:
            if elem in long:
                long.remove(elem)
                ret.append(elem)
        return ret