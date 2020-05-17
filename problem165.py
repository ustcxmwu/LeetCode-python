from typing import List


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = list(map(int, version1.split(".")))
        ver1 = self.clip(ver1)
        ver2 = list(map(int, version2.split(".")))
        ver2 = self.clip(ver2)
        for x, y in zip(ver1, ver2):
            if x > y:
                return 1
            elif x < y:
                return -1
        if len(ver1) > len(ver2):
            return 1
        elif len(ver1) < len(ver2):
            return -1
        else:
            return 0

    def clip(self, ver: List[int]):
        while len(ver) > 0:
            tail = ver.pop()
            if tail != 0:
                ver.append(tail)
                break
        return ver


if __name__ == '__main__':
    version1 = "1.01"
    version2 = "1.001"
    sol = Solution()
    print(sol.compareVersion(version1, version2))