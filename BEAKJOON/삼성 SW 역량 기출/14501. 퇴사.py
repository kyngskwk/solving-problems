import sys

sys.stdin = open("input.txt", "r")

ans = 0

def consult(day, N, cnt, c_list):
    global ans
    if day == N:
        ans = max(cnt, ans)
        return

    for next in range(day, N):
        if next + c_list[next][0] > N:
            ans = max(cnt, ans)
        consult(next + c_list[next][0], N, cnt + c_list[next][1], c_list)


N = int(input())
c_list = [[0, 0] for _ in range(N)]
for i in range(N):
    c_list[i][0], c_list[i][1] = map(int, input().split())

for day in  range(N):
    consult(day + c_list[day][0], N, c_list[day][1], c_list)

print(ans)