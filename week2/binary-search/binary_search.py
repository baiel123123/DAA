class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (right + left) // 2

        while right > left:
            print(left, right, mid)

            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                left = mid + 1
                mid = (right + left) // 2
            else:
                right = mid - 1
                mid = (right + left) // 2

        return mid if nums[mid] == target else -1