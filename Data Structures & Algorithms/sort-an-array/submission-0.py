class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(l, r):
            if l >= r:
                return
            
            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] < pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            quicksort(l, p - 1)
            quicksort(p + 1, r)

        quicksort(0, len(nums) - 1)
        return nums