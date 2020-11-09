class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = collections.defaultdict(int)
        last = collections.defaultdict(int)
        
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        
        max_v = -1
        for k, v in first.items():
            if k in last:
                max_v = max(max_v, last[k] - v - 1)
        return max_v