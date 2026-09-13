class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)

        for stone in stones:
            heapq.heappush(heap,-(stone))

        print(heap)
        lastValue = 0
        while len(heap) > 1:
            val = -heapq.heappop(heap)
            val2 = -heapq.heappop(heap)

            lastValue = max(val,val2) - min(val,val2)

            if not heap:
                break
            if lastValue != 0:
                heapq.heappush(heap,-(lastValue))

            print(lastValue)
            print(heap)
        
        if heap:
            lastValue = -heapq.heappop(heap)
        return lastValue
