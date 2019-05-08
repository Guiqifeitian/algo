class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and not needle:
            return 0
        if not needle:
            return 0
        i = 0
        j = 0
        kmp = self.getNext(needle)
        
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = kmp[j]
        if j == len(needle):
            return i -j
        else:
            return -1
    
    def getNext(self,p):
        kmp = [0 for x in range(len(p))]
        kmp[0] = -1
        i = 0
        k = -1
        while i < len(p) -1:
            if k == -1 or p[i] == p[k]:
                i += 1
                k += 1
                if p[i] == p[k]:
                    kmp[i] = kmp[k]
                else:
                    kmp[i] = k
            else:
                k = kmp[k]
        return kmp

s = Solution()
print s.getNext("abcabdabedaf")
