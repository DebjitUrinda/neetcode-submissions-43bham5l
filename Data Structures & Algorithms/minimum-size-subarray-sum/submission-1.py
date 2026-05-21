class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minWindow = float('inf')
        runSum = 0

        for right in range(len(nums)):
            runSum += nums[right]

            while runSum >= target:
                minWindow = min(minWindow, right - left + 1)

                runSum -= nums[left]
                left += 1

        return 0 if minWindow == float('inf') else minWindow