from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        idx = 0
        while idx < len(A):
            if A[idx] > A[idx + 1]:
                return idx
            idx += 1


