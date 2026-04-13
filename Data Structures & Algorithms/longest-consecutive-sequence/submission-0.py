class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0

        for i in hashSet:
            if i-1 not in hashSet:
                sequence = 1
                while i+sequence in hashSet:
                    sequence += 1
                longest = max(longest, sequence)

        return longest