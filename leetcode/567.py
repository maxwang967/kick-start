class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n_1 = len(s1)
        n_2 = len(s2)
        if n_1 > n_2:
            return False
        pattern_freq = collections.Counter(s1)
        left = 0
        right = n_1 - 1
        text_freq = collections.Counter(s2[:right])
        while right < n_2:
            text_freq[s2[right]] += 1
            if pattern_freq == text_freq:
                return True
            text_freq[s2[left]] -= 1
            if text_freq[s2[left]] == 0:
                del text_freq[s2[left]]
            left += 1
            right += 1
        return False