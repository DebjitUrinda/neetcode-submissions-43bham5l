class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = {}
        freq_s2 = {}
        left = 0

        for c in s1:
            if c not in freq_s1:
                freq_s1[c] = 1
            else:
                freq_s1[c] += 1

        for right in range(len(s2)):
            char = s2[right]
            if char not in freq_s2:
                freq_s2[char] = 1
            else:
                freq_s2[char] += 1

            # If window size exceeds len(s1), remove leftmost character
            if (right - left + 1) > len(s1):
                left_char = s2[left]
                freq_s2[left_char] -= 1

                if freq_s2[left_char] == 0:
                    del freq_s2[left_char]

                left += 1

            if (right-left+1) == len(s1):
                if freq_s1 == freq_s2:
                    return True
            
        return False
