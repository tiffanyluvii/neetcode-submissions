class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1, rob2 = 0,0

        for n in nums:
            temp = max(rob1 + n, rob2)
            # rob1 and rob2 represents the 2 largest sums that can be robbed at that specific point
            rob1 = rob2
            rob2 = temp
        
        return rob2