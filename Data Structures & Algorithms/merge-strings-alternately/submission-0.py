class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # determine the smallest string
        l1 = len(word1)
        l2 = len(word2)

        l = min(l1, l2)

        res = ""
        t = 0

        for i in range(l):
            res += word1[i]
            res += word2[i]
            
            t = i
            l1 -= 1
            l2 -= 1

        if l1:
            res += word1[t+1:]

        elif l2:
            res += word2[t+1:]

        return res