class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ""
        result = strs[0]
        for i in range(1, n):
            j = 0
            while j < len(strs[i]) and j < len(result):
                if strs[i][j] != result[j]:
                    break
                j += 1
            result = result[: j]
            if result == "":
                return ""
        return result
