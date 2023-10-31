## sol1
# from collections import Counter
# import sys
#
# input = sys.stdin.readline
#
# arr = []
# for _ in range(int(input())):
#     arr.append(input())
#
# counter = Counter(arr)
# maxValue = max(counter.values())
#
# answer = []
# for key in counter.keys():
#     if counter[key] == maxValue:
#         answer.append(key)
#
# print(sorted(answer)[0])


## sol2
import sys
dic = dict()

input = sys.stdin.readline

for _ in range(int(input())):
    book = input()

    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 1

maxValue = max(dic.values())

result = []
for key in dic.keys():
    if dic[key] == maxValue:
        result.append(key)

print(sorted(result)[0])
