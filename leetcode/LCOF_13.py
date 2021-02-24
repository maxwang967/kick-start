class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def get_digit_sum(number):
            m_sum = 0
            while number > 0:
                m_sum += number % 10
                number //= 10
            return m_sum

        def movingCountCore(i, j):
            count = 0
            if i >= 0 and i < m and j >= 0 and j < n and (not visited[i * n + j]) and get_digit_sum(i) + get_digit_sum(j) <= k:
                visited[i * n + j] = True
                count = 1 + movingCountCore(i, j + 1) + movingCountCore(i, j - 1) + movingCountCore(i + 1, j) + movingCountCore(i - 1, j) 
            return count

        visited = [False for _ in range(m * n)]
        count = movingCountCore(0, 0)
        return count
