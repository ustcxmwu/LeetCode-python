# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version < 1:
        return False
    else:
        return True

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1

        left = 1
        right = n
        mid = (1+n)//2
        while left < right:
            if isBadVersion(mid):
                right = mid -1
                if not isBadVersion(right):
                    return mid
            else:
                left = mid + 1
                if isBadVersion(left):
                    return left
            mid = (left + right) // 2


if __name__ == '__main__':
    print(Solution().firstBadVersion(3))