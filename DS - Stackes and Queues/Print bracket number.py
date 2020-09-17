def bracketNumbers(S):
    s1 = []
    s2 = []
    x = 0
    for i in range(len(S)):
        if S[i] == '(':
            x += 1
            s1.append(x)
            s2.append(x)
        elif S[i] == ')':
            if len(s2) > 0:
                s1.append(s2.pop())
            else:
                x += 1
                s1.append(x)
    return s1
t = input()
y = bracketNumbers(t)
for i in y:
    print(i)