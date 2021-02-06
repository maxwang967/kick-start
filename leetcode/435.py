class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        intervals.sort(key=lambda x: x[1])
        result = 0
        prev = intervals[0][1]
        for i in range(1, n):
            if intervals[i][0] < prev:
                result += 1
            else:
                prev = intervals[i][1]
        return result