class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        answer = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    m = '0' + str(m) if len(str(m)) == 1 else str(m)
                    answer.append(str(h)+':'+m)
        return answer

"""
- 한 줄로 해결 가능!
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        return [str(h)+':'+'0'*(m<10)+str(m) for h in range(12) for m in range(60) if (bin(m)+bin(h)).count('1') == n]
"""