class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while (left <= right):
            half = left + (right - left) // 2
            print(left)
            print(right)
            print(half)

            if (nums[half] == target):
                return half
            elif (target > nums[half]):
                left = half + 1
            elif (target < nums[half]):
                right = half - 1
            


        return -1
    