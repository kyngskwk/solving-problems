

def solution(n, computers):
    visited = [0] * n
    answer = 0

    def dfs(visited, computers, start):
        stack = [start]
        while stack:
            i = stack.pop()
            visited[i] = 1
            for j in range(0, len(visited)):
                if computers[i][j] == 1 and visited[j] == 0:
                    stack.append(j)

    start = 0
    while 0 in visited:
        if visited[start] == 0:
            dfs(visited, computers, start)
            answer += 1
        start += 1

    return answer