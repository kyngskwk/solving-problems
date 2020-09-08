def solution(N, stages):
    answer = [-1]
    nobody = []
    mans = len(stages)
    stages.sort()
    stage_dict = {}
    now, cnt = stages[0], 0
    for idx in range(mans):
        if now != stages[idx]:
            stage_dict[now] = cnt
            now = stages[idx]
            cnt = 1
            if idx == len(stages)-1:
                stage_dict[stages[idx]] = cnt
        elif idx == len(stages)-1:
            stage_dict[stages[idx]] = cnt + 1
        else:
            cnt += 1

    if stages[-1] < N:
        for s in range(stages[-1]+1, N+1):
            nobody.append(s)

    cnt = 0
    for stage in range(1, stages[-1]+1):
        if stage != N+1:
            if stage in stage_dict:
                answer.append(stage_dict[stage] / (mans - cnt))
                cnt += stage_dict[stage]
            else:
                answer.append(0 / (mans - cnt))

    answer = sorted(range(len(answer)), key=lambda k: answer[k], reverse=True)[:-1]

    if len(nobody) >= 0:
        answer += nobody

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))