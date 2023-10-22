data_list = list(map(int, input().split(' ')))

# 초기화
asc, desc = True, True

# 반복
for index in range(len(data_list)-1):
    if data_list[index] > data_list[index+1]:
        asc = False
    elif data_list[index] < data_list[index+1]:
        desc = False

# print
if asc:
    print("ascending")
elif desc:
    print("descending")
else:
    print("mixed")


"""
0-7
len(size)
len(1, 7)
8 1 7 2 6 3 5 4

"""
