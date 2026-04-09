class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr = 0
        for i in range(len(nums)):
            if nums[i] == val:
                ptr = i
                break

        for j in range(ptr+1, len(nums)):
            if nums[j] != val:
                nums[j], nums[ptr] = nums[ptr], nums[j]
                for l in range(ptr+1, j):
                    if nums[l] == val:
                        ptr = l

        return len(nums[:ptr])