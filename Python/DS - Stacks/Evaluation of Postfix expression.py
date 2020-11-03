def Postfix(expression):
    stack = []
    for i in range(len(expression)):
        element = expression[i]
        if element.isdigit():
            stack.append(int(element))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if element is '+':
                stack.append(operand1 + operand2)
            elif element is '-':
                stack.append(operand1 - operand2)
            elif element is '*':
                stack.append(operand1 * operand2)
            elif element is '/':
                stack.append(operand1 // operand2)
    return stack.pop()


t = int(input())
for _ in range(t):
    expression = input()
    print(Postfix(expression))