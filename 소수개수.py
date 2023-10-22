# 소수 개수 구하기
n = int(input())

list = [0] * (n+1)
cnt = 0
print(list)

for i in range(2, n+1):
  print(i, end=' ')
  if list[i] == 0:
    cnt += 1
    for j in range(i, n+1, i): # ex) 2의 배수만큼
      list[j] = 1
  print(list)
