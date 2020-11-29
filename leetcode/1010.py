class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        r = [0] * 60
        for t in time:
            r[t % 60] += 1
        
        count = 0
        for i, v in enumerate(r):
            if i == 0:
                count += len(list(combinations(range(r[0]), 2)))
            elif i < 60-i and v != 0 and r[60-i] != 0:
                count += (v * r[60-i])
        
        if r[30] != 0:
            count += len(list(combinations(range(r[30]), 2)))
        return count

"""
[빠른 풀이]
- time을 돌면서 각 time마다 pair의 개수를 더해감!
- t가 60으로 나눠질때와 나누어지지 않을때로 구분하는 아이디어!

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0:
                ret += remainders[0]
            else:
                ret += remainders[(60-t) % 60]
            remainders[t % 60] += 1
        
        return ret
"""