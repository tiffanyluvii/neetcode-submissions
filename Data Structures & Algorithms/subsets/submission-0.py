class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combo = []

        def backtrack(index: int, currentArray: List[int]):
            if (index >= len(nums)):
                combo.append(currentArray.copy())
                return


            currentArray.append(nums[index])
            backtrack(index + 1, currentArray)
            currentArray.pop()
            backtrack(index + 1, currentArray)


        backtrack(0, [])
        return combo
