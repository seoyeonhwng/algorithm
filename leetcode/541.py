class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left = 0
        for _ in range(len(s) // (2 * k)):
            right = left + 2 * k
            rotated = s[left:right][:k][::-1] + s[left:right][k:]
            s = s[:left] + rotated + s[right:]
            left += 2 * k
       
        remain = s[left:]
        if len(remain) < k:
            return s[:left] + remain[::-1]
        
        return s[:left] + remain[:k][::-1] + remain[k:]