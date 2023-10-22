"""
3
config.sys
config.inf
configures
"""
N = int(input())
inputList = list([input() for _ in range(N)])

compareData = list(inputList[0])

for i in range(N):
    for j in range(len(compareData)):
        if compareData[j] == inputList[i][j]:
            continue
        else:
            compareData[j] = '?'

print(''.join(compareData))