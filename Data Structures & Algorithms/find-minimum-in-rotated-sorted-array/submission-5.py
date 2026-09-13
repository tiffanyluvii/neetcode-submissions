class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + (right)) // 2

# 3 + 5 - 3 = 5 / 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]
