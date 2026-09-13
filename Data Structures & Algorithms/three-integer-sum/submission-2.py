class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        start = 0

        # [-1 -1 0 1 2 4]
        # start = -1, left = -1, right = 4
        # start = -1, left = -1, right = 2 append to list

        #[-2 0 0 2 2]

        while (start + 1 < len(nums)):
            if (start == 0 or nums[start] != nums[start - 1]):
                currValue = nums[start]
                print("CURR VALUE: " + str(currValue))
                left = start + 1
                right = len(nums) - 1
                while (left < right):
                    if ((currValue + nums[left] + nums[right]) == 0):
                        print("hit 1")
                        output.append([currValue, nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1
                    elif((currValue + nums[left] + nums[right]) > 0):
                        print("hit 2")
                        right -= 1
                    elif((currValue + nums[left] + nums[right]) < 0):
                        print("hit 3")
                        left += 1
            start += 1

        return output

