class Solution:
    # def rob(self, nums: List[int]) -> int:
        
    #     rob1, rob2 = 0,0

    #     for n in nums:
    #         temp = max(rob1 + n, rob2)
    #         # rob1 and rob2 represents the 2 largest sums that can be robbed at that specific point
    #         rob1 = rob2
    #         rob2 = temp
        
    #     return rob2


    def rob(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 0:
            return 0
        if length == 1:
            return nums[0]

        stolen = [0] * length
        stolen[0] = nums[0]
        stolen[1] = max(nums[0], nums[1])

        for i in range(2, length):
            stolen[i] = max(stolen[i - 2] + nums[i], stolen[i - 1])

        return stolen[-1]