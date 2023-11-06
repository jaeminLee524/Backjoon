import sys

input = sys.stdin.readline

N, L = map(int, input().split())
arr = [False] * 1001

for i in map(int, input().split()):
    arr[i] = True

result = 0
x = 0
while x < 1001:
    if arr[x] == True:
        result += 1
        x += L
    else:
        x += 1

print(result)