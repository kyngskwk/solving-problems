import sys

sys.stdin = open('input.txt', 'r')


def find(pan, ans, k, N):
    global visited, my_min
    if k == N:
        my_min = min(my_min, ans)
        return

    else:
        for idx in range(N):
            if visited[idx] == 0 and ans < my_min:
                ans += pan[k][idx]
                visited[idx] = 1
                find(pan, ans, k+1, N)
                visited[idx] = 0
                ans -= pan[k][idx]


for tc in range(1, int(input())+1):
    N = int(input())
    pan = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    my_min = 9999999999999999
    find(pan, 0, 0, N)
    print('#{} {}'.format(tc, my_min))


