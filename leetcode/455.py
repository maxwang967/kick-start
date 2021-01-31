class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i_g = 0
        i_s = 0
        while i_g < len(g) and i_s < len(s):
            if g[i_g] <= s[i_s]:
                i_g += 1
            i_s += 1
        return i_g
