import sys
sys.stdin = open('input.txt', 'r')

ans = 0

def clean(pan, idx, v, i, j):
    global ans

    rot_x = [0, 1, 0, -1]
    rot_y = [-1, 0, 1, 0]

    back_x = [0, -1, 0, 1]
    back_y = [1, 0, -1, 0]
    for k in range(idx+1, idx+5):
        next = k % 4
        # 청소 한 적이 없고, 벽이 아닌 경우
        if pan[i + rot_x[next]][j + rot_y[next]] == 0 and v[i + rot_x[next]][j + rot_y[next]] == 0:
            v[i + rot_x[next]][j + rot_y[next]] = 1
            ans += 1
            clean(pan, next, v, i + rot_x[next], j + rot_y[next])
            return

    # 사 면이 다 청소 되어 있거나, 벽 인 경우
    if pan[i + back_x[idx]][j + back_y[idx]] == 0:
        clean(pan, idx, v, i + back_x[idx], j + back_y[idx])
        return

    # 후진 할 곳도 없다.
    if pan[i + back_x[idx]][j + back_y[idx]] == 1:
        return


N, M = map(int, input().split())
i, j, d = map(int, input().split())
pan = [[] for _ in range(N)]
for x in range(N):
    pan[x] = list(map(int, input().split()))

v = [[0] * M for _ in range(N)]
idx = abs(d - 3)
ans += 1
v[i][j] = 1
clean(pan, idx, v, i, j)
print(ans)

