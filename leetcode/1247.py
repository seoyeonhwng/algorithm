class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1
        
        strings = defaultdict(int)
        for a, b in zip(s1, s2):
            if a != b:
                strings[(a, b)] += 1
        
        answer, res = 0, 0
        for v in strings.values():
            answer, res = answer + (v // 2), res + v % 2
        
        if res % 2 == 1:
            return -1
        return answer + 2 * (res // 2)

