import sys

sys.stdin = open('input.txt', 'r')

def dfs(start, end):
    global visited
    stack = [start]
    while stack:
        next = stack.pop()
        if next == end:
            return 1
        else:
            visited[next] = 1
            for idx in range(1, V+1):
                if pan[next][idx] == 1 and visited[idx] == 0:
                    stack.append(idx)
    return 0


for tc in range(1, int(input())+1):
    V, E = map(int, input().split(' '))
    pan = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split(' '))
        pan[start][end] = 1
    S, G = map(int, input().split())
    visited = [0] * (V+1)

    print('#{} {}'.format(tc, dfs(S, G)))
