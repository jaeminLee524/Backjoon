# def solution(array, commands):
#     answer = []
#     sortData = 0
    
#     # commands에 담긴 배열을 한번식 이용
#     for i in range(len(commands)):
#         arr = commands[i]
#         sortedArray = []
        
#         startIdx, endIdx, sortIdx = arr[0], arr[1], arr[2]
        
#         sortedArray = sorted(array[startIdx-1: endIdx])
#         answer.append(sortedArray.pop(sortIdx-1))
    
#     return answer

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
