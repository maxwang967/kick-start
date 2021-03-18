class Solution:
    def permutation(self, s: str) -> List[str]:
        n = len(s)
        s = list(s)
        result = []

        def dfs(x):
            if x == n - 1:
                result.append("".join(s))
                return
            m_set = set()
            for i in range(x, n):
                if s[i] in m_set:
                    continue
                m_set.add(s[i])
                s[x], s[i] = s[i], s[x]
                dfs(x + 1)
                s[x], s[i] = s[i], s[x]
        dfs(0)
        return result