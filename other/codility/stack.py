def solution(S):
    S = list(S)
    stack = []
    for one in S:
        if one in ['(', '{', '[']:
            stack.append(one)
        else:
            if len(stack) == 0:
                return 0
            elif one == ')' and stack.pop() != '(':
                return 0
            elif one == '}' and stack.pop() != '{':
                return 0
            elif one == ']' and stack.pop() != '[':
                return 0

    if len(stack) != 0:
        return 0
    else:
        return 1

print(solution("[{[()()]}]"))