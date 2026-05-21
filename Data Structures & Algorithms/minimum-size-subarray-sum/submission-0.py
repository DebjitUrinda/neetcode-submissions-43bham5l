class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minWindow, runSum = float('inf'), 0

        # while left <= right:
        #     runSum = 0
        for right in range(len(nums)):
            runSum += nums[right]
            if runSum >= target:
                window = right - left + 1
                while left < right and runSum >= target:
                    window = right - left + 1
                    runSum -= nums[left]
                    left += 1
                    # window = right - left + 1
                    
                minWindow = min(window, minWindow)

        return 0 if minWindow == float('inf') else minWindow