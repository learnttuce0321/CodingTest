def solution(participant, completion):
    answer = ''

    dict = {}

    for i in range(len(participant)):
        if dict.get(participant[i]) is None:
            dict[participant[i]] = 1
        else:
            dict[participant[i]] = dict[participant[i]] + 1

    for i in range(len(completion)):
        dict[completion[i]] = dict[completion[i]] - 1

    
    return [k for k, v in dict.items() if v == 1][0]