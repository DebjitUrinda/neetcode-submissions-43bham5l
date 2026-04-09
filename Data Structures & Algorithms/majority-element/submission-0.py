class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        elem = nums[0]

        for i in range(1,len(nums)):
            if nums[i] == elem:
                count += 1

            elif nums[i] != elem:
                count -= 1

            elif count==0:
                elem = nums[i]

        return elem
