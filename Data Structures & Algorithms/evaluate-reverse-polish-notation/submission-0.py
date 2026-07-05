class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        recent = []
        for val in tokens:
            if val == "+":
                recent.append(recent.pop() + recent.pop())
            elif val == "-":
                a, b = recent.pop(), recent.pop()
                recent.append(b - a)
            elif val == "*":
                recent.append(recent.pop() * recent.pop())
            elif val == "/":
                a, b = recent.pop(), recent.pop()
                recent.append(int(float(b)/a))
            else:
                recent.append(int(val))

        return recent[0]
#### (1, 3, +, 3, -)
#### (4, 3, -)
#value1= 3, value2 = 4 