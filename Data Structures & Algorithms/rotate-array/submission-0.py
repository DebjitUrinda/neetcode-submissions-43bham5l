class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mark = len(nums) - k
        nums[:] = nums[mark:] + nums[:mark]
