def binarySearch(array,value):
    beg = 0
    end = len(array) - 1

    while beg <= end:
        mid = (beg + end) // 2
        if value == array[mid]:
            return mid
        elif value < array[mid]:
            end = mid - 1
        else:
            beg = mid + 1
    else:
        return 'Not Found'

arr = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binarySearch(arr,7))
print(binarySearch(arr,55))

