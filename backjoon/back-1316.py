"""
3
happy
new
year

4
aba
abab
abcabc
a
"""

N = int(input())
inputData = list([input() for _ in range(N)])

result = N

for i in range(N):
    compareData = inputData[i]
    for j in range(len(compareData)-1):
        if compareData[j] == compareData[j+1]:
            continue
        else:
            if compareData[j] in compareData[j+1:]:
                result -= 1
                break

print(result)




# for i in range(N):
#     checkStr = ''
#     compareData = ''
#     for j in range(len(inputDataList[i])):
#         if compareData == '':
#             compareData = inputDataList[i][j]
#             continue
#         if compareData == inputDataList[i][j]:
#             continue
#         else:
#             checkStr += compareData
#             compareData = inputDataList[i][j]
#     checkStr += inputDataList[i][j]
#
#     # 중복 제거 한 인풋데이터와 동일한지
#     if checkStr == ''.join(dict.fromkeys(inputDataList[i])):
#         result += 1
#     checkStr = ''
#
# print(result)