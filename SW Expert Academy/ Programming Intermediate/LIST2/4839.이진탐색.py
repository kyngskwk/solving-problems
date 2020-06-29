import sys

sys.stdin = open("input.txt", "r")

case = int(input())
for i in range(case):
    P, Pa, Pb = list(map(int, input().split()))
    l = 1
    r = P
    c = int((l + r)/2)
    cntA, cntB = 1, 1

    while l <= r:
        if Pa == c:
            break
        elif Pa > c:
            l = c
            c = int((l + r) / 2)
        else:
            r = c
            c = int((l + r) / 2)
        cntA += 1

    l = 1
    r = P
    c = int((l + r) / 2)
    while l <= r:
        if Pb == int((l + r)/2):
            break
        elif Pb > c:
            l = c
            c = int((l + r) / 2)
        else:
            r = c
            c = int((l + r) / 2)
        cntB += 1

    if cntA == cntB:
        print('#{} {}'.format(i + 1, '0'))
    elif max(cntA, cntB) == cntB:
        print('#{} {}'.format(i+1, 'A'))
    elif max(cntA, cntB) == cntA:
        print('#{} {}'.format(i + 1, 'B'))