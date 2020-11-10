class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        def convert(word):
            table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]   
            code = ''
            for w in word:
                code += table[ord(w)-ord('a')]
            return code

        answer = set()
        for w in words:
            answer.add(convert(w))
        return len(answer)