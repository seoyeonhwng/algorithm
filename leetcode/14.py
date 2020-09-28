class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        i = 0
        longest = ''
        shortest = sorted(strs, key=lambda x:len(x))[0]
        
        for i in range(len(shortest)):
            tmp = set([st[i] for st in strs])
            if len(tmp) != 1:
                break
            longest += strs[0][i]
                
        return longest
            
            

"""
[pythonic]

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]; rtype: str
        """
        sz, ret = zip(*strs), ""
        # looping corrected based on @StefanPochmann's comment below
        for c in sz:
            if len(set(c)) > 1: break
            ret += c[0]
        return ret
"""