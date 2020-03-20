from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        map = collections.Counter(s)
        
        for idx,i in enumerate(s):
            
            if map[i]==1:
                return idx
        return -1