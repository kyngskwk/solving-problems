import sys
import math
sys.stdin = open('input.txt', 'r')


def solution(progresses, speeds):
    answer = []
    times = []
    for idx in range(len(progresses)):
        time = math.ceil((100 - progresses[idx]) / speeds[idx])
        times.append(time)

    cnt, idx = 1, 0
    while times:
        front = times.pop(0)
        if len(times) == 0:
            answer.append(cnt)
            break
        else:
            if front >= times[0]:
                while times:
                    if front >= times[0]:
                        times.pop(0)
                        cnt += 1
                    else:
                        break
                answer.append(cnt)
                cnt = 1
            else:
                answer.append(cnt)
                cnt = 1
    return answer

## 다른 방식
def solution2(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

## 다른 방식
def solution3(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]


print(solution([93, 30, 55], [1, 30, 5]))

