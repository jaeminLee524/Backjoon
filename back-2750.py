n = int(input())
array = list()

# 배열 초기화
for _ in range(n):
    array.append(int(input()))

# 정렬
array.sort()

for i in array:
    print(i)

# 선택 정렬
# for i in range(n):
#     min_index = i
#     for j in range(i+1, n):
#         if array[min_index] > array[j]:
#             min_index = j
#             array[i], array[min_index] = array[min_index], array[i]





# 5
# 5
# 2
# 3
# 4
# 1