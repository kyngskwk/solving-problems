import sys

sys.stdin = open("input.txt", "r")

def change(cnt):
    global my_max
    if max_num == num:
        if (t - cnt) % 2 == 0:
            my_max = int(''.join(num))
            return
        else:
            if len(num) == len(set(num)):
                num[-1], num[-2] = num[-2], num[-1]
            my_max = int(''.join(num))
            return

    if cnt == t:
        my_max = max(my_max, int(''.join(num)))
        return

    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] <= num[j]:
                num[i], num[j] = num[j], num[i]
                if v[cnt+1] < int(''.join(num)):
                    v[cnt+1] = int(''.join(num))
                    change(cnt+1)
                num[i], num[j] = num[j], num[i]


for tc in range(1, int(input())+1):
    num, t = map(int, input().split())
    num = list(str(num))
    my_max = 0
    max_num = sorted(num, reverse=True)
    v = [0]*(t+1)
    change(0)
    print('#{} {}'. format(tc, my_max))