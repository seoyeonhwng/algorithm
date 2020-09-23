# brute force로 직접 계산하기
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        if len(s) == 1:
            return count
        
        for window in range(2, len(s)+1):
            for i in range(len(s) - window + 1):
                tmp = s[i:i+window]
                if tmp == tmp[::-1]:
                    count += 1
                    
        return count

# center를 중심으로 확장하면서 개수를 센다
class Solution:
    count = 0
    def count_palindromic(self, left, right, n, s):
        while left >=0 and right < n and s[left] == s[right]:
            self.count += 1
            right += 1
            left -= 1
            
    def countSubstrings(self, s: str) -> int:      
        i = 0
        while i < len(s):
            # 홀수일때 center = (i, i)
            self.count_palindromic(i, i, len(s), s)
            
            # 짝수일때 center = (i-1, i)
            self.count_palindromic(i-1, i, len(s), s)
            i += 1
            
        return self.count
            
        
            