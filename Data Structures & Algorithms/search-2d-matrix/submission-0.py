class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, h = 0, rows*cols-1

        while l<=h:
            mid = (l+h)//2

            row = mid//cols
            col = mid%cols

            val = matrix[row][col]

            if val < target:
                l = mid + 1
            elif val > target:
                h = mid - 1

            elif val == target:
                return True
            # else:
            #     return True

        return False