class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        answer = 0
        
        for k, v in counter.items():
            answer += v * (v - 1) // 2
        return answer

"""
- 처음에는 brute-force 이중 포문으로 풀었음 ㅜㅜ...
"""
