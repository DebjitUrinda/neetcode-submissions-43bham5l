class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        max_freq = 0      # highest frequency in the current window
        max_length = 0    # best answer found so far

        for right in range(len(s)):
            # Add current character to the window
            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                freq[s[right]] += 1

            # Update max frequency in the window
            if freq[s[right]] > max_freq:
                max_freq = freq[s[right]]

            # Shrink window until it becomes valid
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            # Update the best answer
            if right - left + 1 > max_length:
                max_length = right - left + 1

        return max_length