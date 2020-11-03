class Solution:
    def modifyString(self, s: str) -> str:
        def convert(s, i):
            converted = 'a'
            while converted <= 'z':
                if i == 0 and s[i+1] != converted:
                    return converted
                if i == len(s) - 1 and s[i-1] != converted:
                    return converted
                if s[i-1] != converted and s[i+1] != converted:
                    return converted
                converted = chr(ord(converted) + 1)
            return converted
        
        if len(s) == 1:
            return 'a'
        
        for i, c in enumerate(s):
            if c == '?':
                s = s[:i] + convert(s, i) + s[i+1:]
        
        return s