import sys

sys.stdin = open('input.txt', 'r')


def findmax(k, ans, size, N):
    global visited, M, things, my_max
    if k == M:
        my_max = max(my_max, ans)
        return

    if size + things[k][0] <= N and visited[k] == 0:
        visited[k] = 1
        size += things[k][0]
        ans += things[k][1]
        for idx in range(k+1, M+1):
            findmax(idx, ans, size, N)
        visited[k] = 0
        size -= things[k][0]
        ans -= things[k][1]

    elif size + things[k][0] > N:
        my_max = max(my_max, ans)
        return


for tc in range(1, int(input())+1):
    my_max = 0
    N, M = map(int, input().split())
    things = [list(map(int, input().split())) for _ in range(M)]

    visited = [0] * M
    for i in range(M):
        findmax(i, 0, 0, N)
        # visited[i] = 0
    print('#{} {}'.format(tc, my_max))
