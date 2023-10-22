# Baekjoon Online Judge
inputParam = list(input().strip().split(" "))

changeList = []
for element in inputParam:
    changeStr = ""
    for x in element:
        if x.islower():
            changeStr += chr((ord(x) + 13) if x <= 'm' else ord(x) - 13)
        elif x.isupper():
            changeStr += chr((ord(x) + 13) if x <= 'M' else ord(x) - 13)
        else:
            changeStr += x
    changeList.append(changeStr)

printStr = ""
for element in changeList:
    printStr += "".join(element)

print(printStr)
