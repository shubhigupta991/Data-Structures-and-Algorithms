'''Given a sorted array having 10 elements which contains 6 different numbers in which only 1 number is repeated five times.
    Your task is to find the duplicate number using two comparisons only.'''

def findDuplicate(arr,n = 10):
    mid = n // 2
    if arr[mid-1] == arr[mid-2]:
        return arr[mid-1]
    elif arr[mid+1] == arr[mid+2]:
        return arr[mid+1]

t = int(input())
for _ in range(t):
    arr = list(map(int,input().split()))
    print(findDuplicate(arr))