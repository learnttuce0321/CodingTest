def solution(clothes):
    answer = 1
    dict = {}

    for _, c in clothes:
        if c not in dict:
            dict[c] = 1
        else:
            dict[c] += 1

    for item in dict:
        answer *= (dict[item]+1)

    return answer-1