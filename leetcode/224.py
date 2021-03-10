class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        num = 0
        sign = 1
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == "+" or c == "-":
                result += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif c == ")":
                result += sign * num
                num = 0
                result *= stack.pop()
                result += stack.pop()
        result += sign * num
        return result

