import sys

sys.stdin = open('input.txt', 'r')

x, y = map(int, input().split())
A = [0] + [x]
B = [0] + [y]
for tc in range(int(input())):
    K, P = map(int, input().split())
    if K == 0:
        B += [P]
    else:
        A += [P]

print(A, B)

A_max, B_max = 0, 0
A, B = sorted(A), sorted(B)

for idx in range(1, len(A)):
    A_max = max(A_max, A[idx] - A[idx-1])

for idx in range(1, len(B)):
    B_max = max(B_max, B[idx] - B[idx-1])

print(A_max * B_max)