import sys

sys.stdin = open("input.txt", "r")

def right(wheel, idx, dir, temp):
    if idx <= 4 and idx > 1:
        if temp + wheel[idx-1][6] == 1:
            right(wheel, idx + 1, dir * -1, wheel[idx - 1][2])

            if dir == 1:  # 시계 방향
                a = wheel[idx - 1].pop()
                wheel[idx - 1] = [a] + wheel[idx - 1]
            else:
                b = wheel[idx - 1].pop(0)
                wheel[idx - 1] = wheel[idx - 1] + [b]

        else:
            return

def left(wheel, idx, dir, temp):
    if idx >= 1 and idx < 4:
        if wheel[idx-1][2] + temp == 1:
            left(wheel, idx - 1, dir * -1, wheel[idx-1][6])
            if dir == 1:  # 시계 방향
                a = wheel[idx - 1].pop()
                wheel[idx - 1] = [a] + wheel[idx - 1]
            else:
                b = wheel[idx - 1].pop(0)
                wheel[idx - 1] = wheel[idx - 1] + [b]

        else:
            return


wheel = [[] for _ in range(4)]
for idx in range(4):
    wheel[idx] = list(map(int, list(input())))

N = int(input())
c_list  = [[0, 0] for _ in range(N)]
for idx in range(N):
    c_list[idx][0], c_list[idx][1] = map(int, input().split())

for idx, dir in c_list:
    right(wheel, idx+1, dir*-1, wheel[idx-1][2])
    left(wheel, idx-1, dir*-1, wheel[idx-1][6])

    if dir == 1:  # 시계 방향
        a = wheel[idx - 1].pop()
        wheel[idx - 1] = [a] + wheel[idx - 1]
    else:
        b = wheel[idx - 1].pop(0)
        wheel[idx - 1] = wheel[idx - 1] + [b]

ans = 0
for idx in range(4):
    ans += wheel[idx][0] * 2**idx

print(ans)

