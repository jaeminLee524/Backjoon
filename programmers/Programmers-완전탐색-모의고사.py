# def solution(answers):
#     answer = []
#     supoja = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
#     right = [0,0,0]
    
#     for per in range(len(supoja)):
#         for ans in range(len(answers)):
#             perLength = len(supoja[per])
#             if supoja[per][ans%perLength] == answers[ans]:
#                 right[per] += 1
    
#     for idx, score in enumerate(right, start=1):
#         if score == max(right):
#             answer.append(idx)
    
#     return answer

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []
    
    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1
    
    # 기장 많이 맞힌놈을 찾아야됨
    for idx, sc in enumerate(score, start=1):
        if sc == max(score):
            result.append(idx)
            
    return result
