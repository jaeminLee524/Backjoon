def solution(arr1, arr2):
#     row = len(arr1)
#     col = len(arr1[0])
#     answer = [[0]*col for _ in range(row)]

#     for i in range(len(arr1)):
#         for j in range(len(arr1[0])):
#             answer[i][j] = arr1[i][j]+arr2[i][j]
            
    # answer = [c+d for c,d in zip(a,b) for a, b in zip(arr1, arr2)]
    # print(answer)
    
    answer = [[c+d for c,d in zip(a,b)] for a,b in zip(arr1, arr2)]
    return answer
