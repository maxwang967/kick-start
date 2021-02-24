class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def hasCorePath(l, r, c):
            if l == word_length:
                return True
            has_path = False
            if r >= 0 and r < m and c>= 0 and c < n and (not visited[r * n + c]) and board[r][c] == word[l]:
                l += 1
                visited[r * n + c] = True
                has_path = hasCorePath(l, r + 1, c) or hasCorePath(l, r - 1, c) or hasCorePath(l, r, c + 1) or hasCorePath(l, r, c - 1)
                if not has_path:
                    l -= 1
                    visited[r * n + c] = False
            return has_path
                
        word = [w for w in word]
        word_length = len(word)
        m = len(board)
        n = len(board[0])
        visited = [False for _ in range(m * n)]
        path_length = 0
        for row in range(m):
            for col in range(n):
                if hasCorePath(0, row, col):
                    return True
        return False
    
