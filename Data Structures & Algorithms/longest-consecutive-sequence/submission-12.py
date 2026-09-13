class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        consecutive = {}
        unique_set = set(nums)  

        for num in unique_set:
            if num - 1 not in unique_set:
                consecutive[num] = 1


        finish = False
        maximum = 0

        print("begin")
        for key, value in consecutive.items():
            sequence = 1
            current = key
            while not finish:
                if current + 1 in unique_set:
                    sequence += 1
                else:
                    break

                current += 1
                print(sequence)
            
            maximum = max(maximum, sequence)

        return maximum