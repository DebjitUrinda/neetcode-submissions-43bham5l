class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        rotated = [0]*size

        for i in range(size):
            rotated[(i+k)%size] = nums[i]

        nums[:] = rotated[:]
        