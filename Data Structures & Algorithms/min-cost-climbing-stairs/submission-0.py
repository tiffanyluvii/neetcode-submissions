class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        minCost = [0] * len(cost)
        length = len(cost)

        if (len(cost) <= 2):
            return min(cost[0], cost[1])

        reversed_cost = cost[::-1]
        minCost[0] = reversed_cost[0]
        minCost[1] = reversed_cost[1]

        for i in range(2, length):
            minCost[i] = reversed_cost[i] + min(minCost[i-1], minCost[i-2]) 

        return min(minCost[length - 1], minCost[length - 2])
        