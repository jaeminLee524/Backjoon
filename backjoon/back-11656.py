inputStr = input().strip()

prefixList = []

for i in range(0, len(inputStr)):
    prefixList.append(inputStr[i:])

for element in sorted(prefixList):
    print(element)