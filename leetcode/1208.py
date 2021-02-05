class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = len(s)
        s = [x for x in s]
        t = [x for x in t]
        left = 0
        right = 0
        result = 0
        max_cost = 0
        while right < l:
            max_cost += abs(ord(s[right]) - ord(t[right]))
            right += 1
            if max_cost > maxCost:
                max_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            result = max(result, right - left)
        return result
