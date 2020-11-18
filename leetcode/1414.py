class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # k보다 큰 피보나치 수열이 나올때까지 만든다
        # 가장 큰 원소부터 더해가면서 찾는다
        
        nums = [1, 1]
        while nums[-1] < k:
            nums.append(nums[-1] + nums[-2])
        
        count = 0
        while k > 0:
            index = bisect.bisect_right(nums, k) - 1
            k -= nums[index]
            count += 1
        return count
        