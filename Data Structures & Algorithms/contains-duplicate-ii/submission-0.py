class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):
            # If current value is already in the last k elements,
            # we found a duplicate within distance <= k.
            if nums[i] in window:
                return True

            # Add current value to the window.
            window.add(nums[i])

            # Keep only the last k elements.
            if len(window) > k:
                window.remove(nums[i - k])

        return False