class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        window = []

        for right in range(len(arr)):
            window.append(arr[right])

            if len(window) > k:
                a = window[0]
                b = window[-1]

                diff1 = abs(a-x)
                diff2 = abs(b-x)

                if diff1 < diff2 or (diff1 == diff2 and a < b):
                    window.pop()       # remove last element
                else:
                    window.pop(0)

        return window