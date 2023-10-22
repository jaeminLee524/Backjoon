inputData = input().strip() #baekjoon

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for x in alphabet:
    print(inputData.find(x), end=' ')

# for x in alphabet:
#     if x in inputData:
#         print(inputData.index(x), end=' ')
#     else:
#         print(-1, end=' ')
