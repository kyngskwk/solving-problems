import sys

sys.stdin = open("input.txt", "r")


N = int(input())
lights = [0] + list(map(int, input().split()))
nums = int(input())
for num in range(nums):
    K, L = map(int, input().split())
    if K == 1:
        for i in range(L, N+1, L):
            lights[i] = 1 - lights[i]
    else:
        lights[L] = 1 - lights[L]
        x, y = L-1, L+1
        while True:
            if x <= 0 or y >= N+1:
                break
            elif lights[x] != lights[y]:
                break
            else:
                lights[x] = 1 - lights[x]
                lights[y] = 1 - lights[y]
                x -= 1
                y += 1


for idx, i in enumerate(lights[1:]):
    if idx and not(idx % 20):
        print()
    print(i, end=" ")