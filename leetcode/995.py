class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        q = collections.deque()
        result = 0
        N = len(A)
        if N == 0:
            return -1
        for i in range(N):
            if q:
                if i >= q[0] + K:
                    q.popleft()
            if A[i] == len(q) % 2:
                if i + K > N:
                    return -1
                q.append(i)
                result += 1
        return result
            