class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]  # swap with last
                n -= 1                # shrink array
            else:
                i += 1

        return n