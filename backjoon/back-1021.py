"""
10 3
1 2 3

0

10 3
2 9 5

8

32 6
27 16 30 11 6 23

59

10 10
1 6 3 2 7 9 8 4 10 5

14
"""
from collections import deque
N, M = map(int, input().split())
position = list(map(int, input().split()))
# deq = deque([i for i in range(1, N+1)])
inputList = list([i for i in range(1, N + 1)])
result = 0

# for i in range(M):
#     if deq[0] == position[i]:
#         deq.popleft()
#         continue
#     else:
#         if deq.index(position[i]) > (len(deq) // 2):
#             while True:
#                 if deq[0] == position[i]:
#                     deq.popleft()
#                     break
#                 else:
#                     result += 1
#                     deq.appendleft(deq.pop())
#         else:
#             while True:
#                 if deq[0] == position[i]:
#                     deq.popleft()
#                     break
#                 else:
#                     result += 1
#                     deq.append(deq.popleft())
# print(result)

N, M = map(int, input().split())
position = list(map(int, input().split()))
inputList = list([i for i in range(1, N + 1)])
result = 0
for i in range(M):
    # 우로 돌리기
    idx = inputList.index(position[i])
    if idx > len(inputList) // 2:
        result += len(inputList[idx + 1:]) + 1
        inputList = inputList[idx + 1:] + inputList[:idx]
    else: # 좌로
        result += len(inputList[:idx])
        inputList = inputList[idx + 1:] + inputList[:idx]

print(result)

