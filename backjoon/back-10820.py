"""
This is String
SPACE    1    SPACE
 S a M p L e I n P u T
0L1A2S3T4L5I6N7E8

"""

# 10 2 0 2
# 0 10 1 8
# 5 6 0 16
# 0 8 9 0

import sys

while True:
    line = sys.stdin.readline().rstrip('\n')

    if not line:
        break

    l, u, d, s = 0, 0, 0, 0

    for x in line:
        if x.islower():
            l += 1
        elif x.isupper():
            u += 1
        elif x.isdigit():
            d += 1
        elif x.isspace():
            s += 1

    print(l, u, d, s)