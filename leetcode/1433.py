class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        
        check1 = [s1[i] >= s2[i] for i in range(len(s1))]
        check2 = [s1[i] <= s2[i] for i in range(len(s1))]
        
        return all(check1) or all(check2)