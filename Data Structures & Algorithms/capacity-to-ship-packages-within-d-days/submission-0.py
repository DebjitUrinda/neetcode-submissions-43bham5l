class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)      # minimum possible capacity
        high = sum(weights)     # maximum possible capacity

        while low < high:
            mid = (low + high) // 2

            if self.canShip(weights, mid, days):
                high = mid
            else:
                low = mid + 1

        return low

    def canShip(self, weights, capacity, days):
        days_used = 1
        current_load = 0

        for weight in weights:
            if current_load + weight <= capacity:
                current_load += weight
            else:
                days_used += 1
                current_load = weight

        return days_used <= days