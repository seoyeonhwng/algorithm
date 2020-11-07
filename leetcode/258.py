class Solution:
    def addDigits(self, num: int) -> int:
        while int(num) > 9:
            num = sum([int(n) for n in str(num)])
        return int(num)