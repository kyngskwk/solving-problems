import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []
for i in range(N):
    for j in range(N):
        if pan[i][j] == 2: chicken += [(i, j)]


for i in range(N):
    for j in range(N):
        if pan[i][j] == 1: house += [(i, j)]

min_sum = 9999999999999
for c in chicken:
    cnt = 0
    for h in house:
        cnt += abs(c[0]-h[0]) + abs(c[1]-h[1])
    min_sum = min(cnt, min_sum)

print(min_sum)

# 생각!
# 전체를 2차 배열로 받고, 치킨집이 2이다.
# 치킨 집의 좌표가 일단 다 필요하겠다! 집이랑 거리를 구해야하니까!
# 그럼 2가 있는 부분의 좌표를 리스트에 저장한다.
# 여기서 살리는 치킨집의 개수가 정해져 있네! -> 조합을 구해야 하네

# 그 리스트를 for문으로 돌리면서 하나씩 꺼내서
# 전체 판에 있는 가정집들과의 거리를 계산해서 min값을 찾으면 될 것 같다.
# 그럼 가정집이 잇는 좌표도 리스트로 정해놓으면 좋겠지?
