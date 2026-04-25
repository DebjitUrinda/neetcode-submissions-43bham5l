class Solution:
    def isPalindrome(self, s: str) -> bool:
        # regex = [a-zA-Z0-9]
        s_alnum = ""

        for c in s:
            if c.isalnum():
                if c.isalpha():
                    s_alnum += c.lower()
                else:
                    s_alnum += c

        l, r = 0, len(s_alnum)-1
        while l<r:
            if s_alnum[l] != s_alnum[r]:
                return False
            l += 1
            r -= 1

        return True