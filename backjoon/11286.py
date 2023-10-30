import heapq as hq
import sys

## sol 1
# arr = []
# input = sys.stdin.readline
#
# N = int(input())
# for _ in range(N):
#     x = int(input())
#     tuple = ((abs(x)), x)
#
#     if len(arr) == 0 and abs(x) == 0:
#         print(0)
#     elif abs(x) == 0:
#         element = hq.heappop(arr)
#         print(int(element[1]))
#     else:
#         hq.heappush(arr, tuple)


## sol2
arr = []
input = sys.stdin.readline

for _ in range(int(input())):
    x = int(input())

    # x가 0이 아니면
    if x:
        hq.heappush(arr, (abs(x), x))
    else:
        print(hq.heappop(arr)[1] if arr else print)
