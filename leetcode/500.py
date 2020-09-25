class Solution:
    def possible(self, word):
        # whether words can be typed only one row
        first = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        second = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        third = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        
        word = word.lower()
        if all([w in first for w in word]):
            return True
        if all([w in second for w in word]):
            return True
        if all([w in third for w in word]):
            return True
        return False
        
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        for w in words:
            if self.possible(w):
                result.append(w)
        
        return result
                