# 왕자 구하기
n, k = map(int, input().split())
dq = list(range(1, n+1))
dq = deque(dq) # deque 생성

print("dq", dq)


while dq:
  for _ in range(k-1):
    cur = dq.popleft()
    dq.append(cur)
  
  dq.popleft() # k번째 

  if len(dq) == 1:
    break

print("remain deque", dq)
