from collections import deque
dq = deque()

A, B, C, D = list(input().rstrip().split(" "))

firstNum = A+B
secondNum = C+D
print(int(firstNum) + int(secondNum))
