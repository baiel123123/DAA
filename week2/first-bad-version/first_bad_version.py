# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        mid = (right + left) // 2

        while right > left:
            # print(not isBadVersion(mid))
            # print(isBadVersion(mid-1))
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid

            if not isBadVersion(mid):
                left = mid + 1
                mid = (right + left) // 2
            else:
                right = mid - 1
                mid = (right + left) // 2

            # print(left, right, mid)

        return mid