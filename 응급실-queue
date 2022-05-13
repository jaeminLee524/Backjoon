# 환자 수, n번째 환자 index
n, m = map(int, input())

# 환자 목록 
queue = [(pos, val) for pos, val in enumerate(map(int, sys.stdin.readline().rstrip()))]

# dequeu 변환
queue = deque(queue)

# 대기 순서 저장
waitCount = 0
while True:
  cur = queue.popleft()
  # 대기목록과 비교
  if any(cur[1] > x[1] for x in queue): # 뽑은 환자의 위험도가 가장 높음
    waitCount += 1
    if cur[0] == m:
      break
  else: # 목록 환자가 더 높은 경우
    queue.append(cur)

print(m+"번째 환자의 대기순서: ", waitCount)
