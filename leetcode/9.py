class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original = x
        reverse = 0
        
        while x > 0:
            reverse *= 10
            q, r = divmod(x, 10)
            reverse += r
            x = q
        
        return (reverse - original) == 0

# 시간 단축을 위해 x의 절반만 비교해도 된다!
# ex) 1221 이면 절반인 21만 뒤집어서 확인!