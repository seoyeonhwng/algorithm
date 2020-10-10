class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_v = max(candies)
        
        for i in range(len(candies)):
            candies[i] = True if candies[i] + extraCandies >= max_v else False
        
        return candies
            