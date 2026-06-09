class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        rate = 1

        while low < high:
            mid = (low + high) // 2
            # flag = self.canFinish(piles, mid, h)
            if self.canFinish(piles, mid, h):
                high = mid
            else:
                low = mid + 1

            rate = low

        return rate

    def canFinish(self, piles: List[int], k, h) -> bool:
        hours = sum(math.ceil(pile/k) for pile in piles)
        if hours <= h:
            return True

        return False