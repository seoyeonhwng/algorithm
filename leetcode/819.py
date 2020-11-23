class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        str = re.sub(r'[^\w]', ' ', paragraph.lower())
        words = [s for s in str.split(' ') if s and s not in banned]
       
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
            