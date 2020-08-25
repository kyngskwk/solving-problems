def my_dump(dump, box_list):
    for p in range(dump):
        box_list = sorted(box_list)
        box_list[0] += 1
        box_list[-1] -= 1
        if box_list[-1] - box_list[0] == 1:
            break

    box_list = sorted(box_list)
    return box_list[-1] - box_list[0]

case = 10
for i in range(case):
    dump = int(input())
    box_list = list(map(int, input().split()))
    print('#{} {}'.format(i+1, my_dump(dump, box_list)))
