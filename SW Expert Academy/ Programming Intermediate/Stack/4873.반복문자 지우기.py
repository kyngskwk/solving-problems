import sys

sys.stdin = open('input.txt' , 'r')

for tc in range(1, int(input())+1):
    words = input()
    stack = [words[0]]
    for idx in range(1, len(words)):
        if len(stack) >= 1:
            front = stack.pop()
            if front == words[idx]:
                continue
            else:
                stack.append(front)
                stack.append(words[idx])
        else:
            stack.append(words[idx])

    print('#{} {}'.format(tc, len(stack)))

