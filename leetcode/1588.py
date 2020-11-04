class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        window = 1
        total_sum = 0
        
        while window <= len(arr):
            for i in range(len(arr)-window+1):
                total_sum += sum(arr[i:i+window])
            window += 2
        
        return total_sum