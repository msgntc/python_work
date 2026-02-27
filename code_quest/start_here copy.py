import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    data = sys.stdin.readline()

    turky = int(data[0])
    goat = int(data[1])
    horses = int(data[2])
    answer = turky, " ", goat, " ", horses
    total = turky + goat + horses
    print(data)