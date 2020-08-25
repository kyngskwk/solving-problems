import sys

sys.stdin = open('input.txt', 'r')

case = int(input())
for m in range(case):
    N = int(input())
    a = list(map(int, input().split()))
    result = []

    a = sorted(a)

    for k in range(0, 10):
        if k % 2 == 0:
            result.append(a[-((k // 2) + 1)])
        else:
            result.append(a[(k // 2)])

    result = list(map(str, result))

    print('#{} {}'.format(m + 1, ' '.join(result)))