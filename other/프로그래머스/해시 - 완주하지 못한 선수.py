import sys

sys.stdin = open("input.txt", "r")


def solution(participant, completion):
    hash = {}
    for man in participant:
        if man in hash:
            hash[man] += 1
        else:
            hash[man] = 1
    print(hash)
    for man in completion:
        hash[man] -= 1

    for key, value in hash.items():
        if value == 1:
            return key


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))