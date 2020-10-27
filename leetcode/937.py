class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        for l in logs:
            if re.match('[0-9]', l.split(' ')[1]):
                digits.append(l)
            else:
                letters.append(l)
                
        letters.sort(key=lambda x: (x.split(' ')[1:], x.split(' ')[0]))
                
        return letters + digits
            
        