nums = [2,7,11,15]
target = 9

output = []
for i in range(len(nums)):
    print("i:",i, "nums[i]:", nums[i])
    i_val = nums[i]
    for j in range(1, len(nums)):
        if i == j:
            break
        print("j:",j, "nums[j]:", nums[j])
        j_val = nums[j]
        if i_val + j_val == target:
            output.append(i_val)
            output.append(j_val)
            print(output)