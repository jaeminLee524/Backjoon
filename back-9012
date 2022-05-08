import sys

n = int(sys.stdin.readline())

for i in range(n):
  stack = []
  input_data = sys.stdin.readline()
  for j in input_data:
    if j == '(':
      stack.append(j)
    elif j == ')':
      # 스택에 데이터가 존재하는지 체크
      if stack:
        stack.pop()
      else:
        print("NO")
        break

    else:
      if not stack: # 비어있다면
        print("YES")
      else: # 뭔가가 있다면
        print("NO")
