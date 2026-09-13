class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        # [1, 2, 8, 48]
        # [48 ,48 ,24, 6]

        for i, num in enumerate(nums):
            if (i == 0):
                prefix[i] = 1 * num
            else:
                prefix[i] = prefix[i - 1] * num
        
        for i in range(len(nums) - 1, -1, -1):
            print(nums[i])
            print("index: " + str(i))
            if (i == len(nums) - 1):
                postfix[i] = 1 * nums[i]
            else:
                postfix[i] = postfix[i + 1] * nums[i]

        print(prefix)
        print(postfix)

        for i in range(len(nums)):
            if (i == 0):
                output[i] = 1 * postfix[i + 1]
            elif (i == len(nums) - 1):
                output[i] = 1 * prefix[i - 1]
            else:
                output[i] = prefix[i - 1] * postfix[i + 1]

        return output