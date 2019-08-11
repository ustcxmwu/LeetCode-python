class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        common = set1 & set2
        return list(common)





if __name__ == '__main__':
    pass