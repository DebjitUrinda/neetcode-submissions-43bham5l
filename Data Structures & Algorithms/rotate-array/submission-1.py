class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        modVal = k % len(nums)
        mark = len(nums) - modVal
        nums[:] = nums[mark:] + nums[:mark]
