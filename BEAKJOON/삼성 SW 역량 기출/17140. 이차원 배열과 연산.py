import sys
from pprint import pprint
sys.stdin = open("input.txt", "r")


def cal(A):
    max_len = 0
    for idx in range(len(A)):
        num_dict = {}
        for num in A[idx]:
            if num != 0:
                num_dict.setdefault(num, 0)
                num_dict[num] += 1

        num_dict = sorted(num_dict.items())
        num_dict = sorted(num_dict, key=lambda x:x[1])
        if len(num_dict) > 50:
            num_dict = num_dict[0:50]

        A[idx] = [0] * len(num_dict) * 2
        for i in range(len(num_dict)):
            A[idx][2*i], A[idx][2*i + 1] = num_dict[i][0], num_dict[i][1]

        max_len = max(max_len, len(A[idx]))

    for idx in range(len(A)):
        temp = [0]*max_len
        if len(A[idx]) < max_len:
            temp[0:len(A[idx])] = A[idx]
            A[idx] = temp



r, c, k = map(int, input().split())

A = [[0] * 3 for _ in range(3)]
for idx in range(3):
    A[idx] = list(map(int, input().split()))

cnt = 0
while cnt <= 100:
    if len(A) >= r and len(A[0]) >= c:
        if A[r-1][c-1] == k:
            break

    if len(A) >= len(A[0]):
        cal(A)
    else:
        A = list(map(list, zip(*A)))
        cal(A)
        A = list(map(list, zip(*A)))

    cnt += 1

if len(A) >= r and len(A[0]) >= c:
    if A[r-1][c-1] != k:
        print(-1)
    else:
        print(cnt)
else:
    print(-1)