class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for s in S:
            if len(stack) > 0:
                if stack[-1] == s:
                    stack.pop()
                    continue
            stack.append(s)
        return "".join(stack)
