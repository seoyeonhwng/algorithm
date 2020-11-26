class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        if nums:
            self.memo()
            
    def memo(self):
        self.dp = [0] * len(self.nums)
        self.dp[0] = self.nums[0]
        for i in range(1, len(self.nums)):
            self.dp[i] = self.dp[i-1] + self.nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j] - self.dp[i-1] if i > 0 else self.dp[j]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)