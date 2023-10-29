score = [[80, 70], [90, 50], [40, 70], [50, 80]]
score2 = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
def solution(score):

    anwer = sorted([sum(val) for val in score], reverse=True)

    return [anwer.index(sum(val))+1 for val in score]


result = solution(score)
print(result)

def solution(score):

    answer = sorted([sum(val) for val in score], reverse=True)

    print(answer)
    print(answer.index(150))

    return [answer.index(sum(val))+1 for val in score]


result = solution(score2)
print(result)