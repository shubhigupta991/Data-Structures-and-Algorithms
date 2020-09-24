import os
import random
import re
import sys

T = int(input())

for x in range(T):

    N = int(input())

    a = list(map(int, input().split()))

    b = []

    for element in a:
        if element not in b and (-element) not in b:
            b.append(element)

    print(len(b))