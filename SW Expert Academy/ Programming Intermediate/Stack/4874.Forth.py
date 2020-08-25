import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    words = input().split()
    stack = []
    cal = ['+', '-', '/', '*', '.']
    ans = 0
    for idx in range(len(words)):
        if words[idx] not in cal:
            stack.append(int(words[idx]))
        else:
            if len(stack) == 0:
                ans = 'error'
                break
            elif words[idx] == '.':
                if len(stack) > 1:
                    ans = 'error'
                    break
                else:
                    ans = stack.pop()
                    break
            else:
                if len(stack) < 2:
                    ans = 'error'
                    break
                else:
                    a = stack.pop()
                    b = stack.pop()
                    if words[idx] == '+':
                        ans = b + a
                    elif words[idx] == '-':
                        ans = b - a
                    elif words[idx] == '*':
                        ans = b * a
                    else:
                        ans = b // a
                    stack.append(ans)

    print('#{} {}'.format(tc, ans))

