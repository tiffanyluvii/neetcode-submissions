class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        currentArray = []


        def backtrack(index: int, remaining:int):
            if (index < len(nums)):
                if (sum(currentArray) == target):
                    res.append(currentArray.copy())
                    return

                if (nums[index] <= remaining):
                    currentArray.append(nums[index])
                    backtrack(index, remaining - nums[index])
                    currentArray.pop()

                
                backtrack(index + 1, remaining)
                
        backtrack(0, target)
        return res