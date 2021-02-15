class Solution:
    def replaceSpace(self, s: str) -> str:
        # 1 Api
        # return s.replace(" ", "%20")
        # 2 Manually
        s = list(s)
        space_count = 0
        for c in s:
            if c == ' ':
                space_count += 1
        result = [' ' for _ in range(len(s) + 2 * space_count)]
        p_1 = len(s) - 1
        p_2 = len(result) - 1
        while p_1 >= 0 and p_2 >= 0:
            c_1 = s[p_1]
            if c_1 == ' ':
                result[p_2] = '0'
                p_2 -= 1
                result[p_2] = '2'
                p_2 -= 1
                result[p_2] = '%'
                p_2 -= 1
            else:
                result[p_2] = c_1
                p_2 -= 1
            p_1 -= 1
        return ''.join(result)
