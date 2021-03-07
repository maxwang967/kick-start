class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        track = []
        result = []
        def backtrack(t, n):
            if len(t) == len(n):
                result.append(t[:])
                return
            for num in n:
                if num in t:
                    continue
                t.append(num)
                backtrack(t, n)
                t.pop()
        backtrack(track, nums)
        return result