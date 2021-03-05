class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        result = ""

        def palindrome(left, right):
            while left >= 0 and right < N and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        for i in range(N):
            s1 = palindrome(i, i)
            s2 = palindrome(i, i + 1)
            if len(s1) >= len(s2):
                result = s1 if len(result) < len(s1) else result
            else:
                result = s2 if len(result) < len(s2) else result
        return result
        # n = len(s)
        # if n < 2:
        #     return s
        # dp = [[False] * n for _ in range(n)]
        # max_len = 1
        # start = 0

        # for i in range(n):
        #     dp[i][i] = True
        # for j in range(1, n):
        #     for i in range(j):
        #         if s[i] == s[j]:
        #             if j - i < 3:
        #                 dp[i][j] = True
        #             else:
        #                 dp[i][j] = dp[i + 1][j - 1]
        #         else:
        #             dp[i][j] = False
        #         if dp[i][j]:
        #             if (j - i + 1) > max_len:
        #                 max_len = j - i + 1
        #                 start = i   
        # return s[start: start + max_len]