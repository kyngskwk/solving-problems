import sys

sys.stdin = open('input.txt', 'r')

def find(idx, k, N):
    result.append(up[idx])
    result.append(down[idx])
    if k == N-1:
        return

    else:
        find(up.index(down[idx]), k+1, N)


for tc in range(1, int(input())+1):
    N = int(input())
    sets = list(map(int, input().split()))
    up = [0] * N
    down = [0] * N
    for i in range(N):
        up[i] = sets[2*i]
        down[i] = sets[2*i+1]

    result = []

    for i in range(N):
        if up[i] not in down:
            idx = i
            break

    find(idx, 0, N)
    print('#{} {}'.format(tc, ' '.join(list(map(str, result)))))


