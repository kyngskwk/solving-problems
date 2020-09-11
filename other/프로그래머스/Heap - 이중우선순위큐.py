import heapq

def solution(operations):
    answer = []
    heap = []
    for op in operations:
        if op[:1] == 'I':
            heapq.heappush(heap, int(op[2:]))
        elif len(heap) > 0:
            if op == 'D -1':
                heapq.heappop(heap)
            else:
                heap.pop(heap.index(heapq.nlargest(1, heap)[0]))

    if len(heap) > 0:
        answer.append(heap.pop(heap.index(heapq.nlargest(1, heap)[0])))
        answer.append(heapq.heappop(heap))
    else:
        answer = [0, 0]
    return answer

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))