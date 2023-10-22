# 수강 신청, 필수 과목 존재 여부
# 1. 입력 필수과목
# 2. 개수 (플랜개수)
# 3. 테스트 케이스
need = input()
n = int(input())

for i in range(n):
  plan = input() # 수강 계획 
  dequeue = deque(need) # 필수 과목

  for x in plan: # 수강 계획 for
    for d in dequeue: # 필수 과목 for
      if x != dequeue.popleft():
        print("NO")
        break
        
  else: # 포문을 정상적으로 다 돌았을 경우
    if len(dequeue) == 0:
      print("YES")
    else:
      print("NO")
