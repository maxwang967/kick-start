class Solution:
    def clumsy(self, N: int) -> int:
        stack = []
        ops = ["*", "/", "+", "-"]
        for i in range(N, 0, -1):
            if not stack:
                stack.append(i)
                continue
            op = ops[(N - i) % 4 - 1]
            if op == "*":
                stack.append(i * stack.pop())
            elif op == "/":
                stack.append(int(float(stack.pop()) / i))
            elif op == "+":
                stack.append(i)
            elif op == "-":
                stack.append(-i)
        return sum(stack)


