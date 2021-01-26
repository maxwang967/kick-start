class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        memo = {}
        for d in dominoes:
            d.sort()
            if memo.get(str(d)) is None:
                memo[str(d)] = 0
            else:
                memo[str(d)] += 1
        count = 0
        print(memo)
        for k in memo.keys():
            n = memo[k]
            if n >= 1:
                count += (n + 1) * n // 2
        return count
