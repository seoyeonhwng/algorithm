class Solution:
    def maximum69Number (self, num: int) -> int:
        string = str(num)
        for i, n in enumerate(string):
            if n == '6':
                return int(string[:i] + '9' + string[i+1:])
        return num
                