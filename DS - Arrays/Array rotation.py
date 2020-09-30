import math
import os
import random
import re
import sys

T = int(input())

for i in range(T):

    ND = input().split()
    N = int(ND[0])
    D = int(ND[1])

    a = list(map(int, input().split()))

    a.extend(a[:D])
    del (a[:D])

    for j in range(N):
        print(a[j])
    print('')
    
    def rotate(a, d):
    for i in range(d):
        b = a.pop(0)
        a.append(b)
    return a
def max_sum(a,n):
    #code here
    c = []
    sum_arr = []
    for k in range(n):
        summ = 0
        c = rotate(a, k)
        for p in range(len(c)):
            summ += p*c[p]
        sum_arr.append(summ)
    return max(sum_arr)

n = int(input("Enter size: "))
a = list(map(int, input().split()))
print(max_sum(a, n))
