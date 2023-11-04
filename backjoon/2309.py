## sol1
# import sys
# from itertools import permutations

# input = sys.stdin.readline
#
# perArr = []
#
# for _ in range(9):
#     perArr.append(input().strip())
#
# perArr.sort()
#
# answer = []
# for arr in permutations(perArr, 7):
#     int_arr = list(map(int, arr))
#     if sum(int_arr) == 100:
#         answer = int_arr
#         break
#
# sorted_arr = sorted(answer)
# for i in sorted_arr:
#     print(i)



## sol2
# import sys
# from itertools import combinations
#
# input = sys.stdin.readline
# arr = [int(input()) for _ in range(9)]
# answer = []
# for com in combinations(arr, 7):
#     if sum(com) == 100:
#         answer = sorted(com)
#         break
#
# for i in answer:
#     print(i)

## sol3
import sys
input = sys.stdin.readline
arr = [int(input()) for _ in range(9)]
arr.sort()

sum = sum(arr)
def fun():
    for i in range(8):
        for j in range(i + 1, 9):
            if sum - arr[i] - arr[j] == 100:
                for it in range(9):
                    if i != it and j != it:
                        print(arr[it])

                return

fun()