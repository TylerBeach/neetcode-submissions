class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for num in tokens:
            if num == "+":
                b = stack.pop()
                a = stack.pop()
                res = a + b
                stack.append(res)

            elif num == "-":
                a = stack.pop()
                b = stack.pop()
                res = b - a
                stack.append(res)

            elif num == "*":
                b = stack.pop()
                a = stack.pop()
                res = a * b
                stack.append(res)

            elif num == "/":
                a = stack.pop()
                b = stack.pop()
                res = int(float(b) / a)
                stack.append(res)

            else:
                stack.append(int(num))


        return stack[-1]