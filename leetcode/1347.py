class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(t)
        
        counter = counter_t - counter_s
        return sum(counter.values())