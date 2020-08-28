import math
import os
import random
import re
import sys

T = int(input())

for x in range(T):

    N = int(input())

    a = list(map(int, input().split()))

    b =[]
    for i in range(0, N):
        j = a.index(i + 1)
        b.insert(i,j+1)

    for k in range(N):
        print(b[k])
    print()