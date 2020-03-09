from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cnt = dict()
        for idx, num in enumerate(nums):
            tmp = cnt.get(num, list())
            tmp.append(idx)
            cnt[num] = tmp
        dis = float('inf')
        for key, value in cnt.items():
            if len(value) == 1:
                continue
            for idx in range(1, len(value)):
                diff = value[idx] - value[idx - 1]
                dis = diff if diff < dis else dis

        return dis <= k

