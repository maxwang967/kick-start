class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                token = int(token)
                stack.append(int(token))
            except:
                num2 = stack.pop()
                num1 = stack.pop()
                result = 0
                if "+" == token:
                    result = num1 + num2
                elif "-" == token:
                    result = num1 - num2
                elif "*" == token:
                    result = num1 * num2
                elif "/" == token:
                    result = int(num1 / float(num2))
                stack.append(result)
        return stack[0]