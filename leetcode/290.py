class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split(' ')):
            return False
        
        p_table = {} # key : pattern
        s_table = {} # key : s
        
        for st, p in zip(s.split(' '), pattern):
            if st in s_table:
                if p != s_table[st]:
                    return False
            if p in p_table:
                if st != p_table[p]:
                    return False
            if st not in s_table and p not in p_table:
                p_table[p] = st
                s_table[st] = p
        
        return True
                