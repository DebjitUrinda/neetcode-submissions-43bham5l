class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for i in nums:
            if i not in countMap:
                countMap[i] = 1
            else:
                countMap[i] += 1

        sorted_items = sorted(countMap.items(), key=lambda x: x[1], reverse=True)

        output = [item[0] for item in sorted_items[:k]]

        return output