class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        if l == 0:
            return 0
        left = [1 for _ in range(l)]
        right = left[:]
        count = 1
        for i in range(1, l):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            count = left[-1]       
        for i in range(l - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            count += max(left[i], right[i])        
        return count