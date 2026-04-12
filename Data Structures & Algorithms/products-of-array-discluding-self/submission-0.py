class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)

        prefixList = [1] * size
        suffixList = [1] * size
        output = [1] * size

        # Build prefix products
        for i in range(1, size):
            prefixList[i] = prefixList[i - 1] * nums[i - 1]

        # Build suffix products
        for i in range(size - 2, -1, -1):
            suffixList[i] = suffixList[i + 1] * nums[i + 1]

        # Combine
        for i in range(size):
            output[i] = prefixList[i] * suffixList[i]

        return output