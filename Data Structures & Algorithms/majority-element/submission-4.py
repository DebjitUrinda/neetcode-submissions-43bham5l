class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        elem = None

        for i in range(1,len(nums)):
            # print("loop start:", count)
            if count == 0:
                elem = nums[i]

            if nums[i] == elem:
                count += 1
            else:
                count -= 1

            # print("loop ends:", count)

        return elem
