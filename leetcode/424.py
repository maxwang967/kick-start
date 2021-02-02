class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s = [x for x in s]
        l = len(s)
        if l <= 1:
            return l
        left = 0
        right = 0
        freq = [0 for _ in range(26)]
        max_count = 0
        result = 0
        while right < l:
            freq[ord(s[right]) - ord('A')] += 1
            max_count = max(max_count, freq[ord(s[right]) - ord('A')])
            right += 1
            if right - left > max_count + k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            result = max(result, right - left)
        return result
