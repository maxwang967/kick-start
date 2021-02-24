class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def has_core_path(l, r, c):
            if l == word_length:
                return True
            if r >= 0 and r < rows and c >= 0 and c < cols and (not visited[r * cols + c]) and board[r][c] == word[l]:
                l += 1
                visited[r * cols + c] = True
                has_path = False
                has_path = has_core_path(
                    l, r, c + 1
                ) or has_core_path(
                    l, r, c - 1
                ) or has_core_path(
                    l, r + 1, c
                ) or has_core_path(
                    l, r - 1, c
                )
                if not has_path:
                    l -= 1
                    visited[r * cols + c] = False
                return has_path
        rows = len(board)
        cols = len(board[0])
        word = [w for w in word]
        word_length = len(word)
        visited = [False for _ in range(rows * cols)]
        path_length = 0
        for row in range(rows):
            for col in range(cols):
                if has_core_path(path_length, row, col):
                    return True
        return False