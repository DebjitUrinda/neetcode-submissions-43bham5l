class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        elem = nums[0]

        for i in range(1,len(nums)):
            print("loop start:", count)
            if nums[i] == elem:
                count += 1

            elif nums[i] != elem:
                count -= 1
                if count==0:
                    elem = nums[i]
                    count = 1

            print("loop ends:", count)

        return elem
