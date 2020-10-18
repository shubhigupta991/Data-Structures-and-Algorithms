def Prefix(array):
    stack = []
    answer = 0
    for element in array[::-1]:
        if element.isdigit():
            stack.append(int(element))
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            if element == '+':
                stack.append(operand1 + operand2)
            elif element == '-':
                stack.append(operand1 - operand2)
            elif element == '*':
                stack.append(operand1 * operand2)
            elif element == '/':
                stack.append(operand1 / operand2)
    answer = stack.pop()
    return answer

expression = ['-','+','8','/','6','3','2']
print(Prefix(expression))