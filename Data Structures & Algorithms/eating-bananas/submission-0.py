class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxBanana = max(piles)
        lowBanana = 1
        middle = (maxBanana + lowBanana) // 2 
        res = middle

        while maxBanana >= lowBanana:
            currentH = 0
            for bananas in piles:
                currentH += math.ceil(bananas / middle)
            
            if currentH > h:
                lowBanana = middle + 1
            
            else:
                res = middle
                maxBanana = middle - 1

            middle = (maxBanana + lowBanana) // 2 

        return res
