class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first = dict()
        last = dict()
        counter = collections.Counter()
        result = len(nums)
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            counter[num] += 1
        degree = max(counter.values())
        for k, v in counter.items():
            if v == degree:
                result = min(result, last[k] - first[k] + 1)
        return result
