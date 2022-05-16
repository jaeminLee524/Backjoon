# 정다면체 주사위 합 중 나올 수 있는 확률이 가장 높은 숫자
n, m = map(int,input().split(" "))
cnt = [0 for _ in range(n+m+1)]
max = -2147000000

for i in range(1, n+1):
  for j in range(1, m+1):
    cnt[i+j] += 1 # 주사위의 합들의 개수 증가

# 최대값 구하기
for i in range(n+m+1):
  if cnt[i] > max:
    max = cnt[i]

for i in range(n+m+1):
  if cnt[i] == max:
    print(i, end=' ')
