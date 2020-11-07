class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        left, right = 0, len(S)-1
        S = list(S)
        
        while left < right:
            if not S[left].isalpha():
                left += 1
            elif not S[right].isalpha():
                right -= 1
            else:
                S[left], S[right] = S[right], S[left]
                left += 1
                right -= 1
           
        return ''.join(S)