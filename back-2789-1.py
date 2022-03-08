N, M = list(map(int, input().split())) # 5 21
data = list(map(int, input().split())) # 5 6 7 8 9
max_sum = 0

for i in range(len(data)):
    for j in range(i+1, len(data)):
        for k in range(j+1, len(data)):
            result = data[i] + data[j] + data[k]
            if M >= result: # 21 >= 24
                max_sum = max(max_sum, result)
print(max_sum)



