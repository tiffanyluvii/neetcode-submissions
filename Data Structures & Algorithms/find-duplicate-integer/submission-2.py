class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = 0
        fast = 0

        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]

            if (slow == fast):
                break


        secondPointer = 0
        while True:
            slow = nums[slow]
            secondPointer = nums[secondPointer]
            if (slow == secondPointer):
                return slow
        r
            
        