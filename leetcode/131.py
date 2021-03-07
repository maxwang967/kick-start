class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        track = []
        result = []
        def is_palindrome(i, j):
            if i >= j:
                return True
            return is_palindrome(i + 1, j - 1) if s[i] == s[j] else False
        def backtrack(i):
            if i == N:
                result.append(track[:])
                return
            for j in range(i, N):
                if is_palindrome(i, j):
                    track.append(s[i: j + 1])
                    backtrack(j + 1)
                    track.pop()
        backtrack(0)
        return result


