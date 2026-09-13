class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums))]
        result = []
        map = {}

        for num in (nums):
            if (num in map):
                map[num] += 1
            else:
                map[num] =  1

        
        for num in map:
            count[map[num] - 1].append(num)
        
        decrement = len(count) - 1
        while (len(result) < k):
            result += count[decrement]
            decrement -= 1

        return result