
class Solution:

    def count_zeros_and_ones(self, m_str):
        m_list = list(m_str)
        count_zeros = 0
        count_ones = 0
        for d in m_list:
            if d == "0":
                count_zeros += 1
            elif d == "1":
                count_ones += 1
        return count_zeros, count_ones

    def findMaxForm(self, strs, m: int, n: int) -> int:
        l = len(strs)
        # dp[i][j][k]: the size of the largest subset of strs using 1 - i strs, with at most j '0's and k '1's
        dp = [[
            [
                0 for _ in range(0, n + 1)
            ] for _ in range(0, m + 1)
        ] for _ in range(l + 1)]
        dp[5][1][0]
        for i in range(1, l + 1):
            for j in range(0, m + 1):
                for k in range(0, n + 1):
                    # should we contain the i^{th} str?
                    cnt_0, cnt_1 = self.count_zeros_and_ones(strs[i - 1])

                    if cnt_0 <= j and  cnt_1 <= k:
                        # if contain
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - cnt_0][k - cnt_1] + 1)
                        
                    else:
                        # if not contain
                        dp[i][j][k] = dp[i - 1][j][k]
        return dp[l][m][n]

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxForm(
        ["00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01","00","01"],
        50,
        50
    ))