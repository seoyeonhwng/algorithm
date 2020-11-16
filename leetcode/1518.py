class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = numBottles
        
        while numBottles >= numExchange:
            q, r = divmod(numBottles, numExchange)
            numBottles = q + r
            drink += q
        return drink