class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token.isdigit() or len(token)>1:
                stack.append(int(token))
            else:
                num = stack.pop()
                if token == '+':
                    stack[-1] += num
                elif token == '-':
                    stack[-1] -= num
                elif token == '*':
                    stack[-1] *= num
                else:
                    if stack[-1]*num>=0:
                        stack[-1] = abs(stack[-1])/abs(num)
                    else:
                        stack[-1] = -(abs(stack[-1])/abs(num))
        return stack[0]
