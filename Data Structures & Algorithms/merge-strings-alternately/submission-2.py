class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        len1 = len(word1)
        len2 = len(word2)
        k = min(len1, len2)
        res = ""

        while k>0:
            res = res + word1[l] + word2[l]
            l += 1
            r += 1
            k -= 1

        if l == len1:
            res += word2[r:]
        else:
            res += word1[l:]

        return res 
