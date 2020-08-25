import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    A = list(range(1, 13))
    result = 0

    for k in range(1, 1 << len(A)):
        cnt = 0
        sum = 0
        for j in range(len(A) + 1):
            if k & (1 << j):
                cnt += 1
                sum += A[j]
        if cnt == N and sum == K:
            result += 1

    print('#{} {}'.format(tc, result))