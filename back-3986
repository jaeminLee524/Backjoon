import sys
n = int(sys.stdin.readline())
cnt = 0

for i in range(n):
  input_data = sys.stdin.readline().rstrip()
  stack = []

  for j in input_data:
    if stack and j == stack[-1]:
      stack.pop()
    else:
      stack.append(j)
  if not stack:
    cnt += 1
print(cnt)
